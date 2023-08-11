from django.urls import path 
from . import views
from .views import profile

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
    path('profile/', profile, name='dashboard-profile'),
]  
