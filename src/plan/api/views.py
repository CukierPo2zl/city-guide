from django.db.models import Q
from rest_framework.views import APIView
from plan.models import Plan
from attraction.models import Attraction
from .serializers import PlanSerializer, CreatePlanSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins



class PlanAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field      = 'pk'
    serializer_class  = CreatePlanSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        qs = Plan.objects.filter(owner=self.request.user)
        return qs


    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PlanListView(generics.ListAPIView):

    serializer_class  = PlanSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        qs = Plan.objects.filter(owner=self.request.user)
        return qs

