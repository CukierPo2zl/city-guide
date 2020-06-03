from rest_framework import serializers
from attraction.models import Attraction
from django.conf import settings
from city.api.serializers import CitySerializer
from category.api.serializers import CategorySerializer

class AttractionSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Attraction
        fields = [
            'pk',
            'name',
            'description',
            'picture',
            'city',
            'rate',
            'price',
            'category',
            'latitude',
            'longitude',
            'start_h',
            'end_h',
        ]
    def validate_name(self,value):
        qs = Attraction.objects.filter(name=value)
        if qs.exists():
            raise serializers.ValidationError("Nazwa musi być unikalna")
        return value