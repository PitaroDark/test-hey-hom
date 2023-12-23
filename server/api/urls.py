from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'credits/top-up', views.CreditTopUpViewSet, basename='topup')
router.register(r'credits/deduct', views.CreditDeductionViewSet, basename='deduct')
router.register(r'clients', views.ClientsViewSet, basename='clients')
router.register(r'transactions', views.TransactionsViewSet, basename='transactions')

urlpatterns = [
    path('', include(router.urls))
]
