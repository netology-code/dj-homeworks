from django.http import Http404
from requests import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.permissions import isAllowed
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ('update', 'partial_update', 'delete'):
            return [isAllowed()]
        return []

#    def destroy(self, request, *args, **kwargs):
#        instance = self.get_object()
#        self.perform_destroy(instance)
#        return Response(status=status.HTTP_204_NO_CONTENT)

