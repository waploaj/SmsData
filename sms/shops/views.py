from django.shortcuts import render
from .serializers import ShopSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import OsposCustomers, OsposCustomersPoints, OsposCustomersPackages, OsposPeople
from . import serializers

# Create your views here.
@api_view(["GET"])
def all_info(request):
    """Get all the info about customers"""

    shop = OsposCustomers.objects.all()
    serializer = serializers.ShopSerializer(shop, many=True)
    return Response(serializer.data)
