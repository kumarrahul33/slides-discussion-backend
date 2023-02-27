from rest_framework.response import Response
from base.models import SlideQue
from rest_framework.views import APIView
from .serializers import SlideQueSerializer

class SlideQueView(APIView):
    def get(self,request,format=None):
        a=SlideQue.objects.all()
        serializer = SlideQueSerializer(a, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = SlideQueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    