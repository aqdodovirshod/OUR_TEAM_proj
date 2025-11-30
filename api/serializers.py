from rest_framework import serializers

from rest_framework import serializers
from .models import Transaction, UsersProfile, Balance

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("user",) 

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Transaction.objects.create(**validated_data)



class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersProfile
        fields = "__all__"

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'

