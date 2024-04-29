from django.url import path 
from . import views


urlpatterns = [
    path('view9_1/', views.view9_1),
    path('view9_2/', views.view9_2),
]