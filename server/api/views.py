from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import ClientsSerializer, TransactionsSerializer
from .models import Clients, Transactions
from django.shortcuts import get_object_or_404

# Create your views here
class CreditBalanceViewSet(viewsets.ViewSet):
    serializer_class = TransactionsSerializer

    @action(detail=True, methods=['get'])
    def balance(self, request, idClient=None):
        balance = 0
        # Si no hay clientes, respondemos con el balance en 0
        if(Clients.objects.count() == 0):
            return Response({'balance': balance}, status=200)
        client = Clients.objects.get(id=idClient)
        client_transactions = Transactions.objects.filter(client=client)
        # Sumamos todas las transacciones del cliente y respondemos
        for transaction in client_transactions:
            amont = transaction.amont
            balance += amont 
        return Response({'balance': balance}, status=200)

class CreditTopUpViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def list(self, request, *args, **kwargs):
        transactions = Transactions.objects.all().filter(amont__gt=0)
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('client')
        amont = request.data.get('amont')
        user = get_object_or_404(Clients, id=user_id)

        # Crea un nuevo registro para la transacción de recarga de crédito
        transaccion = Transactions.objects.create(client=user, amont=amont)
        # Respondemos con el estandar del serializer
        serializer = self.get_serializer(transaccion)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreditDeductionViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def list(self, request, *args, **kwargs):
        transactions = Transactions.objects.all().filter(amont__lt=0)
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('client')
        amont = request.data.get('amont')
        user = get_object_or_404(Clients, id=user_id)

        # Crea un nuevo registro para la transacción de deducción de crédito
        transaccion = Transactions.objects.create(client=user, amont=-amont)
        # Respondemos con el estandar del serializer
        serializer = self.get_serializer(transaccion)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer   