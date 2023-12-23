from rest_framework import viewsets
from .serializer import ClientsSerializer, TransactionsSerializer
from .models import Clients, Transactions

# Create your views here

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def getBallanceViewSet(id_client: int):
        client = Clients.objects.get(pk=id_client)
        transacciones = Transactions.objects.filter(client=client)
        print(transacciones)
        return {}
    