from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    INCOME='income'
    EXPENSE='expense'

    TRANSACTION_TYPES=[
        (INCOME,'Income'),
        (EXPENSE,'Express'),
    ]
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions'


    )
    title= models.CharField(max_length=100)

    amount= models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    transaction_type=models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    category=models.CharField(max_length=50)

    date=models.DateField()

    notes=models.TextField(blank=True)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.amount}"
    
