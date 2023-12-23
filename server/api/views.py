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
        client = Clients.objects.get(id=idClient)
        client_transactions = Transactions.objects.filter(client=client)
        print(client_transactions, idClient)
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

        # Registrar una transacción de deducción de crédito para el uuario
        transaccion = Transactions.objects.create(client=user, amont=amont)
        # Responder con la confirmación de la transacción y la marca de tiempo
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

        # Registrar una transacción de deducción de crédito para el uuario
        transaccion = Transactions.objects.create(client=user, amont=-amont)
        # Responder con la confirmación de la transacción y la marca de tiempo
        serializer = self.get_serializer(transaccion)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer   