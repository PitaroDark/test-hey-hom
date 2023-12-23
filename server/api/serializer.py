from rest_framework import serializers
from .models import Clients, Transactions

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'