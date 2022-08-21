from django.contrib import admin
from django.urls import path,include
from rest_framework.permissions import IsAuthenticatedOrReadOnly

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/articles/",include("articles.urls")),
    path("api/v1/accounts/",include("accounts.urls")),
]
