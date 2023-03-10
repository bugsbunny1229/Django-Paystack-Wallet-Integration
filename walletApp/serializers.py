from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to validate and create a new user
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
