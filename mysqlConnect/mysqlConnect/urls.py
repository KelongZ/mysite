"""mysqlConnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url, include
from app01 import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register('Updown',views.UpdownViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('ajax_receive/',views.ajax_receive),
    path('ajax_jquery/', views.ajax_jquery),
    path('jquery_get/', views.jquery_get),
    path('up_down/', views.up_down),

# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
    url(r'^data_api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^updown/$',views.UpdownList.as_view(),name='updown'),



    # oauth2 tutorial
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # using re_path
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('accounts/', include('django.contrib.auth.urls')),
]
