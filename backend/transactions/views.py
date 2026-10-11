from decimal import Decimal
from django.db.models import Sum
from rest_framework.decorators import api_view,permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class=TransactionSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
            ).order_by('-date','-id')
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_summary(request):
    user_transactions= Transaction.objects.filter(
        user=request.user
    )
    total_income=(
        user_transactions
        .filter(transaction_type='income')
        .aggregate(total=Sum('amount'))['total']
        or Decimal('0.00')
    )
    total_expense=(
        user_transactions
        .filter(transaction_type='expense')
        .aggregate(total=Sum('amount'))['total']
        or Decimal('0.00')

    )
    balance =total_income - total_expense
    return Response({
        'total_income':str(total_income),
        'total_expenses':str(total_expense),
        'balance':str(balance),
    })

