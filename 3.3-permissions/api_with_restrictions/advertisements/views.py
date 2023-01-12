from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favorite
from advertisements.permissions import IsOwner, IsOwnerDraft
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    @action(detail=False, permission_classes=[IsAuthenticated])
    def favorites(self, request):
        queryset = Advertisement.objects.filter(favorites__owner=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        ad = self.get_object()
        user = request.user

        if user == ad.creator:
            raise ValidationError('You cannot add your listings to favorites')

        if Favorite.objects.filter(owner=user, ad=ad).ordered:
            raise ValidationError('This ad is already in your favorites')

        Favorite.objects.create(owner=user, ad=ad)
        return Response('Ad added to favorites')

    def get_queryset(self):
        if self.request.user.pk is None:
            self.queryset = Advertisement.objects.filter(draft=False)
        else:
            self.queryset = Advertisement.objects.filter(Q(creator=self.request.user) | Q(draft=False))
        return self.queryset

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsOwner()]
        else:
            return [IsOwnerDraft()]
