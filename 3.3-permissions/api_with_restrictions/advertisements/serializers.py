from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, Favorite


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
                  'status', 'created_at', 'draft')

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # Обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # Само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        validated_data["favorites"] = False
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        request = self.context['request'].method
        user = self.context['request'].user

        if request == 'POST' and Advertisement.objects.filter(creator=user, status='OPEN').count() >= 10:
            raise ValidationError('You cannot create more than 10 open ads')

        return data


class FavoriteSerializer(serializers.ModelSerializer):
    '''Serializer для избранного.'''

    owner = UserSerializer(read_only=True, )
    # ad = AdvertisementSerializer(read_only=True, )

    class Meta:
        model = Favorite
        fields = ('id', 'owner', 'ad')
