from rest_framework import serializers
from plan.models import Plan
from django.conf import settings


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'owner',
            'track',
            'start_hour',
            'end_hour',
            'final_time',     
        ]
    