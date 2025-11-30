from accounts.models import CustomUser
from django.db import models
    
class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, related_name='transactions', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        balance = Balance.objects.filter(user=self.user).first()
        if not balance:
            balance = Balance.objects.create(user=self.user, amount=0)
        if self.transaction_type == 'EXPENSE':
            if balance.amount >= self.amount:
                balance.amount -= self.amount
        else:
            balance.amount += self.amount
        balance.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"


class UsersProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Balance(models.Model):
    user = models.OneToOneField(CustomUser, related_name='balance', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username
