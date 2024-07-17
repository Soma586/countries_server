import requests
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MessageSerializer

@api_view(['GET'])
def get_region_data(request, region):
    url = f'https://restcountries.com/v3.1/region/{region}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data)
    else:
        return Response({'error': 'Region not found'}, status=response.status_code)

@api_view(['GET'])
def get_name_data(request, name):
    url = f'https://restcountries.com/v3.1/name/{name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Response(data)
    else:
        return Response({'error': 'country not found'}, status=response.status_code)
