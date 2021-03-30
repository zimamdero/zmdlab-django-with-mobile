from django.urls import path
from card_v1 import views


urlpatterns = [
    path('card-list-public/', views.CardV1ListPublicView.as_view(), name='card_list_public'),
    path('card-list/', views.CardV1ListView.as_view(), name='card_list'),
    path('card/<int:pk>/', views.CardV1View.as_view(), name='card'),
    path('card-add/', views.CardV1AddView.as_view(), name='card_add'),
    path('img-info/<int:pk>/', views.CardV1View.as_view(), name='img_info'),
    path('img-info-add/', views.ImgInfoAddView.as_view(), name='img_info_add'),
]