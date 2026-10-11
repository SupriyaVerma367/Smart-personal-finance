from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction

        fields=[
            'id',
            'title',
            'amount',
            'transaction_type',
            'category',
            'date',
            'notes',
            'created_at',
        ]
        read_only_fields=['id','created_at']
