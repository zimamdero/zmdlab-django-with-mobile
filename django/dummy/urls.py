from django.urls import path
from dummy.views import HelloView, PublicHelloView


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('hello/public/', PublicHelloView.as_view(), name='hello_public'),
]