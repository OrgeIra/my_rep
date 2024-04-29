from django.urls import path
from . import views

urlpatterns = [
    path('view4_1/', views.view4_1),
    path('view4_2/', views.view4_2),
]