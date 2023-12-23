from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.ClientsViewSet)
router.register(r'transactions', views.TransactionsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
