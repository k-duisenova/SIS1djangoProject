from django.urls import path
from . import views

# after reading inputs calculate page opens and outputs result
urlpatterns = [
    path('', views.home, name='home'),
    path('calculate', views.calculate, name='calculate')
]