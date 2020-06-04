from rest_framework import serializers
from ordered_attraction.models import OrderedAttraction
from attraction.api.serializers import AttractionSerializer

class OrderedAttractionSerializer(serializers.ModelSerializer):

    attraction = AttractionSerializer(read_only=True)

    class Meta:
        model = OrderedAttraction
        fields = [
            'attraction',
            'order',
            'travel_time',
            'travel_length'
        ]

class CreateOrderedAttractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedAttraction
        fields = [
            'attraction',
            'order',
            'travel_time',
            'travel_length'
        ]
