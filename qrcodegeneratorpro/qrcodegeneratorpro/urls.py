"""
URL configuration for qrcodegeneratorpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from qr_generatorapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.registratonPage),
    path('registratonPage',views.registratonPage,name='registratonPage'),
    path('loginPage',views.loginPage,name='loginPage'),
    path('qr_generatorPage',views.qr_generatorPage,name='qr_generatorPage'),
    path('download_qr/<str:text>/',views.download_qr, name='download_qr'),
    path('logoutpage',views.logoutpage,name='logoutpage'),
]
