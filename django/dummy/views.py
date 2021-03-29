from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class PublicHelloView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)