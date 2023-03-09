from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', 'updated_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        adv_creator = self.context["request"].user
        limit_advertisement_count = 10
        # TODO: добавьте требуемую валидацию
        open_advertisement = Advertisement.objects.filter(creator=adv_creator) & Advertisement.objects.filter(status=AdvertisementStatusChoices.OPEN)
        advertisement_count = open_advertisement.count()
        if advertisement_count > (limit_advertisement_count - 1):
            raise serializers.ValidationError("У Вас-{} уже {} активных объявлений, достигнут лимит. Объявление не добавлено".format(adv_creator, advertisement_count))
    
        return data
