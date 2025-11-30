from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, UsersProfile, Balance
from .serializers import (
    TransactionSerializer,
    UsersProfileSerializer,
    BalanceSerializer
)

class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UsersProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile, _ = UsersProfile.objects.get_or_create(user=self.request.user)
        return profile


class BalanceView(generics.RetrieveAPIView):
    serializer_class = BalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        balance, _ = Balance.objects.get_or_create(user=self.request.user)
        return balance
    
class FilterTransactionView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Transaction.objects.filter(user=self.request.user)
        t_type = self.request.query_params.get('type')
        if t_type:
            qs = qs.filter(transaction_type=t_type)
        return qs
