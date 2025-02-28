"""
URL configuration for course project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings  # Import the settings module
from django.conf.urls.static import static
from course import views  # Import the views module from the course directory
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt decorator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/home/', login_required(views.home), name='home'),  # محافظت از مسیر هوم با login_required
    path('post/', include('post.urls', namespace='post')),
    path('', include('django.contrib.auth.urls')),  # تنظیم صفحه لاگین به عنوان صفحه اول
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
