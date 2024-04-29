from django.urls import path
from . import views

urlpatterns = [
    path('view5_1/', views.view5_1),
    path('view5_2/', views.view5_2),
]