import django_filters
from advertisements.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator', 'status', 'created_at']
