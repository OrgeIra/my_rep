from django.urls import path
from . import views

urlpatterns = [
    path('view2_1/', views.view2_1),
    path('view2_2/', views.view2_2),
]
