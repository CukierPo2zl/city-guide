from rest_framework import serializers
from plan.models import Plan
from accounts.api.serializers import _UserDetailSerializer
from ordered_attraction.api.serializers import OrderedAttractionSerializer, CreateOrderedAttractionSerializer
from ordered_attraction.models import OrderedAttraction

class CreatePlanSerializer(serializers.ModelSerializer):
    owner = _UserDetailSerializer(read_only=True)
    route = CreateOrderedAttractionSerializer(many=True)

    class Meta:
        model = Plan
        fields = [
            'owner',
            'route',
            'route_length'
        ]

    def create(self, validated_data):
        r = validated_data.pop('route')

        instance = Plan.objects.create(owner=self.context['request'].user, **validated_data)
        instance.save()
        for obj in r:
            tmp = OrderedAttraction.objects.create(
                attraction=obj['attraction'],
                order=obj['order'],
                travel_time=obj['travel_time'],
                travel_length=obj['travel_length']

            )
            instance.route.add(tmp)

        return instance

class PlanSerializer(serializers.ModelSerializer):
    owner = _UserDetailSerializer(read_only=True)
    route = OrderedAttractionSerializer(many=True)

    class Meta:
        model = Plan
        fields = [
            'pk',
            'owner',
            'route',
            'route_length'
        ]
