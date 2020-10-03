from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Room


# class RoomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=140)
#     price = serializers.IntegerField()
#     bedrooms = serializers.IntegerField()
#     instant_book = serializers.BooleanField()

class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)

