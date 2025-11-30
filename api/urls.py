from django.urls import path
from .views import TransactionListCreateView ,TransactionDetailView , ProfileView ,BalanceView,FilterTransactionView
urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view()),
    path('transactions/<int:pk>/', TransactionDetailView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('balance/', BalanceView.as_view()),
    path('transactions/filter/', FilterTransactionView.as_view()),
]
