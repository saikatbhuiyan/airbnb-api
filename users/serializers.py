from rest_framework import serializers

from .models import User


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "superhost",
        )


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "is_staff",
            "is_active",
            "date_joined",
            "favs",
        )


class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def validate_first_name(self, value):
        print(value)
        return value.upper()