from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_1, name='about'),
    path('order/', views.order, name='order'),
    path('FAQ/', views.faq, name='FAQ'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('add/', views.add, name='add'),
]