from django.urls import path
from .register import UserRegister, UserLogin, UserLogout
from .views import UserList

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('users/', UserList.as_view(), name='users'),
]