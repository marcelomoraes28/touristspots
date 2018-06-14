from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer
from rest_framework.filters import SearchFilter


class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filter_fields = ('name', 'description')
    filter_backends = (SearchFilter,)
    search_fields = ('description', 'address__line1')

