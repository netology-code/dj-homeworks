from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    id = filters.ModelMultipleChoiceFilter(
        field_name='id',
        to_field_name='id',
        queryset=Advertisement.objects.all()
    )

    status = filters.ChoiceFilter(
        field_name='status',
        choices=AdvertisementStatusChoices.choices
    )

    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
