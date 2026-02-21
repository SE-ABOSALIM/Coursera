from rest_framework import serializers
from .models import Foods
from decimal import Decimal

class FoodsSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='origin')
    price_after_tax = serializers.SerializerMethodField()
    class Meta:
        model = Foods
        fields = ['id', 'name', 'country', 'price', 'price_after_tax']

    def get_price_after_tax(self, product:Foods):
        taxed_price = product.price * Decimal('1.10')
        return taxed_price.quantize(Decimal('0.00'))

class FoodsFilteredSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)