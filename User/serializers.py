from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        return User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()


# user login registacia serialikzerit
# views modelei djangoti
# url
