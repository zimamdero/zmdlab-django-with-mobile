from rest_framework import serializers
from django.contrib.auth.models import User
from user_auth.models import UserProfile, UEmailAuth
from user_auth.common.validation import emailValidate, passwordValidate
from user_auth.common.raiseobj import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'email', 'date_joined', 'is_active']

    def update(self, instance, validated_data):
        if hasattr(validated_data, 'email'):
            instance.email = validated_data.get('email', instance.email)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        try:
            user = User.objects.get(id=obj.user.id)
            return UserSerializer(user).data
        except Exception as e:
            return {
                "exception": e.args
            }

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'user_img', 'greetings',
                  'created_at', 'updated_at']
        lookup_field = 'user'


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email')

    def validate(self, attrs):
        user = self.context['request'].user
        email = attrs['email']
        if User.objects.exclude(pk=user.pk).filter(email=email).exists():
            raise serializers.ValidationError(email_already_use())

        if User.objects.exclude(pk=user.pk).filter(username=attrs['username']).exists():
            raise serializers.ValidationError(username_already_use())

        if emailValidate(attrs['email']) == False:
            raise serializers.ValidationError(email_not_validate())

        uEmailAuth = UEmailAuth.objects.get(email=email)
        if uEmailAuth.auth_num_check == False:
            raise serializers.ValidationError(uemail_auth_num_check_not_complete())

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(password_fields_not_match())

        if passwordValidate(attrs['password']) == False:
            raise serializers.ValidationError(password_not_validate())

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.create(user=user)

        return user


class PasswordChangingSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(password_fields_not_match())

        if passwordValidate(attrs['password']) == False:
            raise serializers.ValidationError(password_not_validate())

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(old_password_not_correct())
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError(authorize_fail())

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    greetings = serializers.CharField(required=False)
    user_img = serializers.ImageField(use_url=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'greetings', 'user_img')

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError(authorize_fail())

        if hasattr(validated_data, 'user'):
            user_data = validated_data.pop('user')
            user = User.objects.get(pk=user.pk)
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.update(user, user_data)

        if hasattr(validated_data, 'greetings'):
            instance.greetings = validated_data.get('greetings', instance.greetings)

        if hasattr(validated_data, 'user_img'):
            instance.user_img = validated_data.get('user_img', instance.user_img)

        instance.save()

        return instance
