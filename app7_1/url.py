from django.url import path
from . import views

urlpatterns = [
    path('view7_1/', views.view7_1),
    path('view7_2/', views.view7_2),
]