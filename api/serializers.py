from rest_framework import serializers

from rest_framework import serializers
from .models import Transaction, UsersProfile, Balance

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'amount', 'transaction_date', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        transaction = Transaction.objects.create(user=user, **validated_data)
        return transaction


class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersProfile
        fields = ['id', 'bio', 'phone_number', 'address']

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['id', 'amount']

