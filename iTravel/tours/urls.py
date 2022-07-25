from django.urls import path
from .views import (
    ToursListView,
    ToursUpdateView,
    ToursDetailView,
    ToursDeleteView,
    ToursCreateView,
    OrdersView,
    OrderCreate,
    OrdersDoneView
)

urlpatterns = [
    path('<int:pk>/edit/', ToursUpdateView.as_view(), name='tour_edit'),
    path('<int:pk>/', ToursDetailView.as_view(), name='tour_detail'),
    path('<int:pk>/delete/', ToursDeleteView.as_view(), name='tour_delete'),
    path('new/', ToursCreateView.as_view(), name='tour_create'),
    path('done/', OrdersDoneView.as_view(), name='order_done'),
    path('orders-list/', OrdersView.as_view(), name='orders_list'),
    path('<int:pk>/order/', OrderCreate.as_view(), name='order'),
    path('', ToursListView.as_view(), name='tours_list')
]