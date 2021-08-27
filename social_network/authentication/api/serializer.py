from django.core import exceptions
from django.contrib.auth import authenticate
from django.core import exceptions
from django.utils.translation import gettext as _
from django.contrib.auth import password_validation

from rest_framework import serializers
from rest_auth.serializers import PasswordResetConfirmSerializer

from custom_user.models import CustomUser

class CustomRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, )
    first_name = serializers.CharField(max_length=150, required=True)
    age = serializers.IntegerField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate_email(self, email):
        user = CustomUser.objects.filter(email=email).exists()
        if user:
            raise serializers.ValidationError(_('This Email has already been registed'))
        else:
            return email

    def validate_password(self, password):
        try:
            password_validation.validate_password(password=password)
            return password
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(_('Password must include number, character and at least 8 lenght.'))

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError(_('Age must be at least 18.'))
        else:
            return age

    def validate_first_name(self, first_name):
        """
            Add first name validate
        """
        return first_name

    def save(self, request):
        return super().save()

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            age=validated_data['age']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = None
        user = self.authenticate(email=email, password=password)

        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        email_address = user.emailaddress_set.get(email=user.email)
        if not email_address.verified:
            raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs

class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    uid = None
    token = None
    def validate(self, attrs):
        attrs['uid'] = self.context['view'].kwargs['uidb64']
        attrs['token'] = self.context['view'].kwargs['token']
        return super().validate(attrs)    
