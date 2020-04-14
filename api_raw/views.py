from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import testrawmodel

# Create your views here.
def index(request):
    return HttpResponse("api_raw index")

def test_raw(request):
    '''
    Returns a serialized model queryset
    '''
    testdata = testrawmodel.objects.all()
    testdata_serialized = serializers.serialize('json', testdata)
    return HttpResponse(testdata_serialized, content_type="application/json")

def test_raw_only_values(request):
    '''
    Returns a list of model values
    '''
    testdata = testrawmodel.objects.all().values()
    print(testdata)
    testdata_list = list(testdata)
    print(testdata_list)
    return JsonResponse( testdata_list, safe=False )
