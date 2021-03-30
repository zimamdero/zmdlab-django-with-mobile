from django.urls import path
from card_v1 import views


urlpatterns = [
    path('card-list/', views.CardV1ListView.as_view(), name='card_list'),
    path('card/<int:pk>/', views.CardV1View.as_view(), name='card'),
]