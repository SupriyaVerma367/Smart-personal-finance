from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import TransactionViewSet,dashboard_summary

router=DefaultRouter()
router.register(
    r'',
    TransactionViewSet,
    basename='transaction'

)

urlpatterns=[
     path('summary/',dashboard_summary,name='dashboard-summary'),
    path('',include(router.urls)),
   
]