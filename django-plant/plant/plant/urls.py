"""plantBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('plantapp/', include('plantapp.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    #If you're intending to use the browsable API you'll probably also want to 
    #add REST framework's login and logout views. Add the following to your root urls.py file.
    path('api-auth/', include('rest_framework.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
