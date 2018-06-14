from rest_framework import serializers
from attractions.models import Attraction


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'initial_period', 'minimum_age',
                  'photo')


