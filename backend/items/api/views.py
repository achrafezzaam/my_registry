from rest_framework.viewsets import ModelViewSet
from .serializers import ItemSerializer
from ..models import Item

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
