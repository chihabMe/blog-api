from collections import UserList
from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import *

app_name='accounts'
urlpatterns=[
    path("token/",TokenObtainPairView.as_view(),name='token_obtain'),
    path("token/refresh/",TokenRefreshView.as_view(),name='token_refresh'),
    path("token/verify/",TokenVerifyView.as_view(),name='token_verify'),
    path("",UserListView.as_view(),name='user_list'),
]