from django.urls import path
from . import views

urlpatterns = [
    path('view3_1/', views.view3_1),
    path('view3_2/', views.view3_2),
]
