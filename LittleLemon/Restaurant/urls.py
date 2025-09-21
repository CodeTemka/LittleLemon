from django.urls import path
from .views import bookingView, menuView

urlpatterns = [
    path('bookings/', bookingView.as_view(), name='bookings'),
    path('menu/', menuView.as_view(), name='menu'),
]