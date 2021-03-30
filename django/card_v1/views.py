from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from card_v1.serializers import *


class CardV1ListPublicView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        cards = CardV1.objects.filter(level=1)
        result = [CardV1Serializer(card).data for card in cards]
        return Response(result)


class CardV1ListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        userid = request.user.id
        cards = CardV1.objects.filter(writer=userid)
        result = [CardV1Serializer(card).data for card in cards]
        return Response(result)


class CardV1View(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardV1.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CardV1Serializer


class CardV1AddView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CardV1Serializer


class ImgInfoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImgInfo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ImgInfoSerializer


class ImgInfoAddView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImgInfoSerializer
