from plan.models import Plan
from .serializers import PlanSerializer, CreatePlanSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics, mixins
from django.http.response import JsonResponse
from rest_framework.decorators import api_view



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

@api_view(['DELETE'])
def plan_delete(request, pk):
    try:
        plan = Plan.objects.get(pk=pk)
    except Plan.DoesNotExist:
        return JsonResponse({'message': 'The plan does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        plan.delete()
        return JsonResponse({'message': 'Plan was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
