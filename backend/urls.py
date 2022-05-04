"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'kingdoms', views.KingdomView, 'kingdom')
router.register(r'phylums', views.PhylumView, 'phylum')
router.register(r'classes', views.ClassNameView, 'class')
router.register(r'orders', views.OrderView, 'order')
router.register(r'genuses', views.GenusView, 'genus')
router.register(r'families', views.FamilyView, 'family')
router.register(r'scientificnames', views.ScientificNameView, 'scientificname')
router.register(r'classifications', views.ClassificationView, 'classification')
router.register(r'conservationstatuses', views.ConservationStatusView, 'conservationstatus')
router.register(r'facts', views.FactView, 'fact')
router.register(r'physicalcharacteristics', views.PhysicalCharacteristicsView, 'physicalcharacteristic')
router.register(r'locations', views.LocationView, 'location')
router.register(r'animals', views.AnimalView, 'animal')
router.register(r'images', views.ImageView, 'image')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
