from django.urls import path
from . import views

urlpatterns =[
    path('', views.apiOverview),
    path('customer_list/', views.customerList),
    path('create_customer/', views.createCustomer),
]
