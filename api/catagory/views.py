from rest_framework import viewsets
from .serializers import CatagorySerializer
from .models import Catagory


class CatagoryViewSet(viewsets.ModelViewSet):
    queryset = Catagory.objects.all().order_by('name')
    serializer_class = CatagorySerializer
