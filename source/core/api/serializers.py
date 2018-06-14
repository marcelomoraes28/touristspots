from rest_framework import serializers
from core.models import TouristSpot


class TouristSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = ('name', 'description', 'approved', 'attractions',
                  'address', 'photo')
