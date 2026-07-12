from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('authorised-distributor/', views.authdistributor, name='authorised-distributor'),
    path('partner-clients/', views.partnerclients, name='partner-clients'),
    path('products/', views.products, name='products'),
    path('contactus/', views.contactus, name='contactus'),
    # path('contact/', views.contact, name='contact'),
    path('contactus/', views.contactus, name='contactus'),
]