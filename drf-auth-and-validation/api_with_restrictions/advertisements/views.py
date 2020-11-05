from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.permissions import isAllowed
from advertisements.serializers import AdvertisementSerializer

from django.db.models import When


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

  #  queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        queryset = Advertisement.objects.all()
        user = self.request.user
        print(user.id)
        if user.id is None:
            return queryset.exclude(status='DRAFT')
        #elif queryset.filter(status='DRAFT'):
         #   return queryset.filter(creator_id=user.id).all()
        #elif queryset.filter(status='DRAFT'):
        #    return queryset.exclude(status="DRAFT", creator_id=user.id)



    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ('update', 'partial_update', 'delete'):
            return [isAllowed()]
        return []
