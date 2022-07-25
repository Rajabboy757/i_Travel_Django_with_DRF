from rest_framework import serializers
from .models import Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('title', 'cost', 'days', 'nights', 'start_date', 'country')
