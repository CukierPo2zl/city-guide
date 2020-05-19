from django.db.models import Q
from rest_framework import generics, mixins
from plan.models import Plan
from attraction.models import Attraction
from .serializers import PlanSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny


class PlanAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field      = 'pk'
    serializer_class  = PlanSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        qs = Plan.objects.all()
        query = self.request.GET.get("owner")
        if query:
            qs = qs.filter(Q(owner=query))
        return qs



    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PlanRUDView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field      = 'pk'
    serializer_class  = PlanSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        qs = Plan.objects.all()
        query = self.request.GET.get("owner")
        qs = qs.filter(owner=self.request.user)
        return qs


