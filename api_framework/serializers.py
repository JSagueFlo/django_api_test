from rest_framework import serializers
from .models import testmodel

class testSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = testmodel
        fields = '__all__'