from rest_framework import serializers

from API.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
     id = serializers.ReadOnlyField()

     class Meta:
         model=Company
         fields="__all__"

