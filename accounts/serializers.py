from rest_framework import serializers, response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

User = get_user_model()

USER_TYPE_CHOICES = (
    (1, 'admin'),
    (2, 'reader'),
)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'user_type')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if not user.exists:
            raise ValidationError('email exists')
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password2 != password:
            raise ValidationError('passwords do not match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    # def create(self, validated_data):
    #     email = validated_data['email']
    #     password = validated_data['password']
    #     user = authenticate(email=email, password=password)
    #     if user:
    #         token, _ = Token.objects.get_or_create(user=user) #if token exists it returns the token if not creates
    #         return response.Response({
    #             'token': token.key
    #         })
    #     raise ValidationError('User does not exist!')

