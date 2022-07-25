from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Tour, Order
from rest_framework import generics

from .serializers import TourSerializer


class ToursListView(ListView):
    model = Tour
    template_name = 'tours_list.html'


class ToursDetailView(DetailView):
    model = Tour
    template_name = 'tour_detail.html'


class ToursUpdateView(UpdateView):
    model = Tour
    fields = ('title', 'description', 'cost', 'days', 'nights', 'start_date', 'country', 'free_places',)
    template_name = 'tour_edit.html'


class ToursDeleteView(DeleteView):
    model = Tour
    template_name = 'tour_delete.html'


class ToursCreateView(CreateView):
    model = Tour
    fields = ('title', 'description', 'cost', 'days', 'nights', 'start_date', 'country', 'free_places', 'image',)
    template_name = 'tour_create.html'


class OrdersView(ListView):
    model = Order
    template_name = 'orders_list.html'

class OrdersDoneView(TemplateView):
    model = Order
    template_name = 'order_done.html'

class OrderCreate(CreateView, DetailView):
    model = Order
    fields = ('tour', 'client_name',)
    template_name = 'order.html'

    def get_initial(self):
        name = self.request.user
        return {
            'client_name': name,
        }


class ToursAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer