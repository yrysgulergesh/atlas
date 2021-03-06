from django.urls import path, include
from atlasmak.views import *
# from atlasmak.views import CompanyListAPIView, CertificateListAPIView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('catalog', CatalogViews)


urlpatterns = [
    path('', include(router.urls)),
    path('company/', CompanyListAPIView.as_view(), name='company-list'),
    # path('certificate/', CertificateListAPIView.as_view(), name='certificate-list'),
    path('catalog/', CatalogListAPIView.as_view(), name='catalog-list'),
    path('parameter/', ParameterListAPIView.as_view(), name='parameter-list'),
    path('delivery/', DeliveryListAPIView.as_view(), name='delivery-list'),
    path('contacts/', ContactsListAPIView.as_view(), name='contact-list'),
]