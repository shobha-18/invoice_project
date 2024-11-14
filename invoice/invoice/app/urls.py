from django.urls import path
from . import views

urlpatterns = [
    path('api/invoices/', views.invoice_create_update, name='invoice_create_update'),
]
