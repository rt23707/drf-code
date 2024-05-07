
from django.shortcuts import render
from rest_framework import viewsets

from API.serializers import CompanySerializer
from API.models import Company
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



