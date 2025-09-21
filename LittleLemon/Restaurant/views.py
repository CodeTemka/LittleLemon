from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
# Create your views here.

class bookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = bookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class menuView(APIView):
    def get(self, request):
        menu_items = Menu.objects.all()
        serializer = menuSerializer(menu_items, many=True)
        return Response(serializer.data)
