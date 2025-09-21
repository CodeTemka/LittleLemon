from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
# Create your views here.
