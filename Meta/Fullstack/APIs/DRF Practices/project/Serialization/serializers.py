from rest_framework import serializers
from .models import Food, MenuItem, Category
from decimal import Decimal

class FoodsSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='origin')
    calculated_tax = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = ['id', 'name', 'country', 'price', 'calculated_tax']

    def get_calculated_tax(self, product:Food):
        taxed_price = product.price * Decimal('1.10')
        return taxed_price.quantize(Decimal('0.00'))

class FoodsFilteredSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)

# ----------------------------------------------------------------------------------

# Relationship Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer): # PASS HERE
    stock = serializers.IntegerField(source='inventory')
    calculated_tax = serializers.SerializerMethodField()
    # This part creates a hyperlink refers to name='category-detail' named url. Instead of that, it could be done by passing (serializers.HyperlinkedModelSerializer) to "PASS HERE"
    category = serializers.HyperlinkedRelatedField (
        queryset = Category.objects.all(),
        view_name='category-detail',
    )
    # category = CategorySerializer(read_only=True) # uncomment to perform post request in api/menu-items and cpmment the above one
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock',  'calculated_tax', 'category']
        # depth=1 # same as (category = CategorySerializer()). This way you don't need the CategorySerializer

    def get_calculated_tax(self, product:MenuItem):
        taxed_price = product.price * Decimal('1.10')
        return taxed_price.quantize(Decimal('0.00'))