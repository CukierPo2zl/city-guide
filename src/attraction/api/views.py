from django.db.models import Q
from rest_framework import generics, mixins
from attraction.models import Attraction
from .serializers import AttractionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from city.models import City
from category.models import Category

class AttractionAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field      = 'pk'
    serializer_class  = AttractionSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        qs = Attraction.objects.all()
        city_name = self.request.GET.get("city")
        category_name = self.request.GET.get("category")
        if city_name and category_name:
            _filter_city = City.objects.get(name=city_name)
            _filter_category = Category.objects.get(name=category_name)
            qs = qs.filter(Q(city=_filter_city))
            qs = qs.filter(Q(category=_filter_category))
        if city_name:
            _filter = City.objects.get(name=city_name)
            return qs.filter(Q(city=_filter))
        if category_name:
            _filter = Category.objects.get(name=category_name)
            return qs.filter(Q(category=_filter))
        return qs



    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AttractionRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field      = 'pk'
    serializer_class  = AttractionSerializer
    permission_classes = [AllowAny]



    def get_queryset(self):
        return Attraction.objects.all


# Wyswietla 4 najpopularniejsze atrakcje turystyczne tzn.
# najwyższa ocena/liczba ocen
class TrendingAttractions(generics.ListAPIView):
    serializer_class = AttractionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = Attraction.objects.all()
        return qs[0:5]









