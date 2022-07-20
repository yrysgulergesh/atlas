from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# class CertificateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Certificate
#         fields = '__all__'       

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'  


class CatalogSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Catalog
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'  


# class VisitNumberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VisitNumber
#         fields = '__all__' 


# class DayNumberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DayNumber
#         fields = '__all__' 