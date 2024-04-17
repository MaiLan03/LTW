from django.urls import path
from . import views

urlpatterns = [
    # Các patterns khác nếu có
    path('dsnhansu/', views.dsnhansu, name='dsnhansu'),
]
