from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from accounts.models import User
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from accounts.api.serializers import UserSerializer, _UserDetailSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.decorators import api_view
from category.models import Category
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'update':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or  self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class EditView(generics.RetrieveUpdateDestroyAPIView):
   lookup_field = 'pk'
   serializer_class = _UserDetailSerializer

   def get_queryset(self):
       return User.objects.all()


