from django.contrib import admin
from django.urls import path,include
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/articles/",include("articles.urls")),
    path("api/v1/accounts/",include("accounts.urls")),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)