# Thus Serialisers are gonna be classes that take a certain model that we want to serialize or object and its gonna turn it into json data and we can return that

from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'



