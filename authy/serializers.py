from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = UserModel
        exclude = ("is_superuser", "is_staff", "is_active", "date_joined",
                   "groups", "user_permissions", "updated", "last_login")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if ("password" in data) and ("confirm_password" not in data) or ("password" not in data) and ("confirm_password" in data):
            raise serializers.ValidationError(
                "password and confirm password are not mutually exclusive and must be submitted together.")

        if ("password" in data) and ("confirm_password" in data) and (data["password"] != data["confirm_password"]):
            raise serializers.ValidationError(
                "password and confirm password must match.")

        return data

    def save(self, **kwargs):
        self.validated_data.pop("confirm_password", None)
        return super().save(**kwargs)

    def create(self, validated_data):
        from django.db import transaction

        with transaction.atomic():
            user = super().create(validated_data)
            user.set_password(user.password)
            user.save(update_fields=["password"])

            return user

