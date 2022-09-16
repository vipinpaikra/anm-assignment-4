
from django.urls import path,include
from account.views import UserLoginView, UserProfileView, UserRegistrationView,LogoutView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('logout/', LogoutView.as_view(),name='logout'),

   
]
  