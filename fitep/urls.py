"""fitep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_simplejwt import views as jwt_views
from fitep.settings import MEDIA_URL, MEDIA_ROOT




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls')),
    path('api/course/', include('course.api.urls')),
    path('api/branch/', include('branch.api.urls')),
    path('api/chat/', include('chat.api.urls')),
    path('api/package/', include('package.api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + staticfiles_urlpatterns()

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
