from django.db.models import Q
from rest_framework import generics, mixins
from attraction.models import Attraction
from .serializers import AttractionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class AttractionAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field      = 'pk'
    serializer_class  = AttractionSerializer
    permission_classes = [AllowAny]





    def get_queryset(self):
        qs = Attraction.objects.all()
        query = self.request.GET.get("city")
        query1 = self.request.GET.get("category")
        if query and query1:
            qs = qs.filter(Q(city=query))
            qs =qs.filter(Q(category=query1))
        return qs



    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AttractionRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field      = 'pk'
    serializer_class  = AttractionSerializer
    permission_classes = [AllowAny]



    def get_queryset(self):
        return Attraction.objects.all()