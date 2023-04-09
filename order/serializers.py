from rest_framework import serializers
from .models import Order



class OrderSerializer(serializers.ModelSerializer):
    size = serializers.CharField()
    status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta: 
        model = Order
        fields = ['size','status','quantity']



class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField()
    status = serializers.CharField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta: 
        model = Order
        fields = ['size','status','quantity']



class UpdateOrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(default='PENDING')
    class Meta:
        model = Order
        fields = ['status']



class OrderView(serializers.ModelSerializer):
    