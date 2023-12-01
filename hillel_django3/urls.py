"""
URL configuration for hillel_django3 project.

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

import products.views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from products.viewsets import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', products.views.hello_world),
    path('product-count/', products.views.count_product),
    path('product-json/', products.views.count_product_json),
    path('api/', include(router.urls))
]
