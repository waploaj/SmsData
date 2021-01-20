from rest_framework import serializers
from .models import OsposCustomers

class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = OsposCustomers
        field = '__all__'