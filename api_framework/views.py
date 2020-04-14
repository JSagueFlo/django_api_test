from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import testmodel
from .serializers import testSerializer

# Create your views here.
def index(request):
    return HttpResponse("api_framework index")

class Test(APIView):
    '''
    Returns data from the testmodel via rest_framework utilities
    '''
    def get(self, request):
        testdata = testmodel.objects.all()
        serializer = testSerializer(testdata, many=True)
        return Response(serializer.data)
