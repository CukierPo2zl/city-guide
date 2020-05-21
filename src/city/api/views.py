from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CitySerializer
from city.models import City

class CitiesView(ListAPIView):
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return City.objects.all()