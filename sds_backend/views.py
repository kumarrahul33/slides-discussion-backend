from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import SlideQue
from .serializers import SlideQueSerializer

@api_view(['GET'])
def getData(request):
    a=SlideQue.objects.all()
    serializer = SlideQueSerializer(a, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = SlideQueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)