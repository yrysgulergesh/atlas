from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import *

from .serializer import CompanySerializer, CatalogSerializer, DeliverySerializer, ContactsSerializer


class CompanyListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        company = Company.objects.all()
        company_json = CompanySerializer(company, many=True)
        return Response(data=company_json.data)



# class CertificateListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         certificate = Certificate.objects.all()
#         certificate_json = CertificateSerializer(certificate, many=True)
#         return Response(data=certificate_json.data)


class CatalogListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        catalog = Catalog.objects.all()
        catalog_json = CatalogSerializer(catalog, many=True)
        return Response(data=catalog_json.data)


class DeliveryListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        delivery = Delivery.objects.all()
        delivery_json = DeliverySerializer(delivery, many=True)
        return Response(data=delivery_json.data)


# class VisitNumberListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         visit_number = VisitNumber.objects.all()
#         visit_number_json = VisitNumberSerializer(visit_number, many=True)
#         return Response(data=visit_number_json.data) 


# class DayNumberListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         day_number = DayNumber.objects.all()
#         day_number_json = DayNumberSerializer(day_number, many=True)
#         return Response(data=day_number_json.data) 
class ContactsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        contacts = Contacts.objects.all()
        contacts_json = ContactsSerializer(contacts, many=True)
        return Response(data= contacts_json.data)

class CatalogViews(ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
