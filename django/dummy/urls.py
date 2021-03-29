from django.urls import path
from dummy.views import HelloView


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
]