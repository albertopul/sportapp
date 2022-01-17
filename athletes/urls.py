from django.urls import path
from . import views


urlpatterns = [
    path('', views.athletes, name="athletes"),
    path('athlete/<str:pk>/', views.athlete, name="athlete"),
    path('create-athlete/', views.createAthlete, name="create-athlete"),
    path('update-athlete/<str:pk>/', views.updateAthlete, name="update-athlete"),
    path('delete-athlete/<str:pk>/', views.deleteAthlete, name="delete-athlete"),
]
