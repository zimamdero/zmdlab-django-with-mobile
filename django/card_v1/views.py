from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from card_v1.serializers import *


class CardV1ListPublicView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CardV1Serializer

    def get_queryset(self):
        return CardV1.objects.filter(level=1).order_by('-created_at')


class CardV1ListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CardV1Serializer

    def get_queryset(self):
        userid = self.request.user.id
        return CardV1.objects.filter(writer=userid).order_by('-created_at')


class CardV1View(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardV1.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CardV1Serializer


class CardV1AddView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CardV1Serializer


class CardV1ListAddView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        cardList = request.data['list']
        for card in cardList:
            serializer = CardV1Serializer(data=card)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)


class ImgInfoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImgInfo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ImgInfoSerializer


class ImgInfoAddView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImgInfoSerializer


class ImgInfoListAddView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        infoList = request.data['list']
        for info in infoList:
            serializer = ImgInfoSerializer(data=info)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)