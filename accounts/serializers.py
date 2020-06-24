from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'email'
        )

    # class UserSerializer(serializers.HyperlinkedModelSerializer):

    #     class Meta:
    #         model = User
    #         fields = ('url', 'email', 'first_name',
    #                   'last_name', 'password', 'profile')
    #         extra_kwargs = {'password': {'write_only': True}}

    #     def create(self, validated_data):
    #
    #         password = validated_data.pop('password')
    #         user = User(**validated_data)
    #         user.set_password(password)
    #         user.save()
    #         return user

    #     def update(self, instance, validated_data):
    #         profile_data = validated_data.pop('profile')
    #         profile = instance.profile

    #         instance.email = validated_data.get('email', instance.email)
    #         instance.save()

    #         return instance
