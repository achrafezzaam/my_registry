from rest_framework.serializers import ModelSerializer
from ..models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'company', 'body', 'email', 'status', 'category', 'date')
