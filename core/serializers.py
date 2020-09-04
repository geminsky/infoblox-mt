from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from core import models


class DataSerializer(serializers.ModelSerializer):
    """
    Serializer for the model Data

    """
    guid = serializers.UUIDField(required=False)

    class Meta:
        model = models.Data
        fields = ['guid', 'enabled']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the model Users
    Data serializer is used as nested serializer

    """
    id = serializers.IntegerField(read_only=True)
    data = DataSerializer(many=True)

    class Meta:
        model = models.Users
        fields = ['id', 'first_name', 'last_name', 'city', 'data']
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):

        """

        :param validated_data:
        :return: object

        """

        datum = validated_data.pop("data")
        data_list = []
        for data in datum:
            try:
                try:
                    user_data = models.Data.objects.get(guid=data['guid'])
                except ObjectDoesNotExist:
                    user_data = models.Data.objects.create(enabled=data['enabled'])
                    user_data.guid = data['guid']
                    user_data.save()
                data_list.append(user_data)
            except Exception as e:
                print(e)
                user_data = models.Data.objects.create(enabled=data['enabled'])
                data_list.append(user_data)
        user = models.Users.objects.create(**validated_data)
        user.data.set(data_list)
        return user
