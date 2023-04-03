from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
# HTTP METHODS THAT ARE ALLOWED TO ACCESS THIS VIEW (THUS ONLY A GET REQUEST)
def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)
# safe means we can use more than just python dict inside this response
# safe is gonna allow this list to be turned into a json list

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

# objects cannot be converted automatically to json format

# here many means that Are there going to be multiple objects that we need to serialize or just one

@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

# return a single array