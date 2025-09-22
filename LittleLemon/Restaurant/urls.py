from django.urls import path
from .views import bookingView, menuView
from . import views
from rest_framework import routers
from .views import UserViewSet
from django.urls import include

from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('bookings/', bookingView.as_view(), name='bookings'),
    path('menu/', menuView.as_view(), name='menu'),
    path('protected/', views.protected_view, name='protected'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
