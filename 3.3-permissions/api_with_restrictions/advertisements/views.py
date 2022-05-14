import django_filters
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement

from advertisements.serializers import AdvertisementSerializer


class OnlyOwnerDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return obj.creator_id == request.user.id  # prevent fetching whole user model
        return True  # anyone can do any other action


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), OnlyOwnerDeletePermission()]
        return []

