from rest_framework import viewsets

from .serializers import KarthikSerializer
from .models import KarthikModel

class KarthikViewSet(viewsets.ModelViewSet):
    queryset = KarthikModel.objects.all()
    serializer_class = KarthikSerializer
