from django.urls import path
from user_auth import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.SignUpView.as_view(), name='auth_signup'),
    path('signout/', views.SignOutView.as_view(), name='auth_signout'),
    path('user/<int:pk>/', views.UserView.as_view(), name='user_detail'),
    path('user-profile/<int:user>/', views.UserProfileView.as_view(), name='user_profile_detail'),
    path('user-info/', views.UserInfoView.as_view(), name='user_info'),
    path('change-password/<int:pk>/', views.PasswordChangingView.as_view(), name='change_password'),
    path('update-user-profile/<int:pk>/', views.UpdateUserProfileView.as_view(), name='update_user_profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout-all/', views.LogoutAllView.as_view(), name='logout_all'),
    path('uemail-auth-number/', views.UEmailAuthNumberView.as_view(), name='uemail_auth_number'),
    path('uemail-auth/', views.UEmailAuthView.as_view(), name='uemail_auth'),
]