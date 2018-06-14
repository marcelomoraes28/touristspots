"""tourist URL Configuration

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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import TouristSpotViewSet
from django.conf import settings
from django.conf.urls.static import static
from address.api.viewsets import AddressViewSet
from attractions.api.viewsets import AttractionViewSet
from comments.api.viewsets import CommentViewSet
from evaluations.api.viewsets import EvaluationViewSet


router = routers.DefaultRouter()
router.register(r'touristspot', TouristSpotViewSet, base_name='TouristSpot')
router.register(r'address', AddressViewSet)
router.register(r'attractions', AttractionViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'evaluation', EvaluationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



