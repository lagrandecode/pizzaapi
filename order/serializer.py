from rest_framework import serializers
from .models import *



class OrderSerializer(serializer.ModelSerializer):
    size = serializers.CharField(max_length=20)
    status = serializers.HiddenField(max_length=20,default='PENDING')
    quantity = serializers.PositveIntergerField()
    class Meta: 
        model = Order
        fields = ['size','status','quantity']