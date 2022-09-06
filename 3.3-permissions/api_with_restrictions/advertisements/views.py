from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner, IsOwnerDraft
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

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
