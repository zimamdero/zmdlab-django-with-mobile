from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from user_auth.serializers import *
from user_auth.models import UserProfile, UEmailAuth
from random import randrange
from django.core.mail import EmailMessage
from user_auth.common.validation import emailValidate
from user_auth.common.raiseobj import email_not_validate
from user_auth.common.timechecker import uemail_auth_num_time_check

from django.utils import timezone


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    lookup_field = 'user'


class PasswordChangingView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangingSerializer


class UpdateUserProfileView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializers_class = UpdateUserProfileSerializer



class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class SignOutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        User.objects.filter(id=request.user.id).delete()

        return Response(status=status.HTTP_205_RESET_CONTENT)


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        userid = request.user.id
        profile = UserProfile.objects.get(user=userid)
        return Response(UserProfileSerializer(profile).data)


class UEmailAuthNumberView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data['email']
        if emailValidate(email) == False:
            return Response(email_not_validate())

        if User.objects.filter(email=email).exists():
            emailMessage = EmailMessage('Email auth number requested',
                                        'There was email auth number request by your email [%s]' % email,
                                        to=[email])
            emailMessage.send()
            return Response(email_already_use(), status=status.HTTP_400_BAD_REQUEST)

        auth_num = '%d' % randrange(10)
        auth_num += '%d' % randrange(10)
        auth_num += '%d' % randrange(10)
        auth_num += '%d' % randrange(10)
        auth_num += '%d' % randrange(10)
        auth_num += '%d' % randrange(10)

        obj, created = UEmailAuth.objects.get_or_create(email=email)
        obj.auth_num = auth_num
        obj.auth_num_check = False
        obj.save()

        emailMessage = EmailMessage('Email auth number', '%s' % auth_num, to=[email])
        emailMessage.send()
        return Response({
            #'auth_num': auth_num,
            'message': 'sending auth number to your email [%s]' % email
        })


class UEmailAuthView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data['email']
        auth_num = request.data['auth_num']
        obj = UEmailAuth.objects.get(email=email)

        if not obj:
            return Response(uemail_has_not_email(), status=status.HTTP_400_BAD_REQUEST)

        if auth_num != obj.auth_num:
            return Response(uemail_auth_num_incorrect(), status=status.HTTP_400_BAD_REQUEST)

        if uemail_auth_num_time_check(obj.updated_at) == False:
            return Response(uemail_auth_num_time_over(), status=status.HTTP_400_BAD_REQUEST)

        obj.auth_num_check = True
        obj.save()

        return Response(success())
