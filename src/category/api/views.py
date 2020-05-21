from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import CategorySerializer
from category.models import Category

class CategoriesView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Category.objects.all()