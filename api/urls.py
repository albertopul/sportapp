from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    
    path('athletes/', views.getAthletes),
    path('athletes/<str:pk>/', views.getAthlete),
    
    path('clubs/', views.getClubs),
    path('clubs/<str:pk>/', views.getClub),

    path('remove-sponsor/', views.removeSponsor)
]