from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import CurrentUserDefault
from .models import (
    Category, MenuItem,
    Cart, Order, OrderItem,
)
import bleach

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

    def validate_title(self, value):
        return bleach.clean(value)

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'stock', 'category']

    def validate_title(self, value):
        return bleach.clean(value)

    def validate_price(self, value):
        if value < 1.00:
            raise serializers.ValidationError('Price should not be less than 1.00')
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('Stock cannot be negative')
        return value

class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    final_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'quantity', 'unit_price', 'final_price', 'user', 'menuitem']
        validators = [
            UniqueTogetherValidator(
                queryset=Cart.objects.all(),
                fields=['user', 'menuitem']
            )
        ]

    def create(self, validated_data):
        menuitem = validated_data['menuitem']
        validated_data['unit_price'] = menuitem.price
        validated_data['final_price'] = menuitem.price * validated_data['quantity'] * 0.1
        return super().create(validated_data)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'total', 'date', 'user', 'delivery_crew']

class OrderItemSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    final_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'unit_price', 'final_price', 'order', 'menuitem']
        validators = [
            UniqueTogetherValidator(
                queryset=OrderItem.objects.all(),
                fields=['order', 'menuitem']
            )
        ]