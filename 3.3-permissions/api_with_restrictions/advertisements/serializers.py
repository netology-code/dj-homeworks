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
                  'status', 'created_at',)

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

        # TODO: добавьте требуемую валидацию
        user = self.context["request"].user
        advertisement_qnt = Advertisement.objects.filter(creator=user, status=AdvertisementStatusChoices.OPEN).count()
        if self.instance is not None:
            if self.instance.creator != user:
                raise serializers.ValidationError("You do not have permission to perform this action.")
            advertisement_status = data.get("status")
            if advertisement_status is not None:
                if advertisement_status == AdvertisementStatusChoices.OPEN and advertisement_qnt >= 10:
                    raise serializers.ValidationError("Слишком много объявлений!")
        else:
            if advertisement_qnt >= 10:
                raise serializers.ValidationError("Слишком много объявлений!")

        return data


