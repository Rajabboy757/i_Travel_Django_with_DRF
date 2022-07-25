from django.db import models
from django.urls import reverse


class Tour(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    days = models.PositiveIntegerField()
    nights = models.PositiveIntegerField()
    start_date = models.DateField()
    country = models.CharField(max_length=20)
    free_places = models.PositiveIntegerField()

    # broned_users = models.JSONField(default=dict)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tour_detail', args=[str(self.id)])


class Order(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='orders')
    client_name = models.CharField(max_length=30)
    order_date = models.DateTimeField(auto_now_add=True)
    payed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('order_done',)