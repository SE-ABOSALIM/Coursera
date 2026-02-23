from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import Food, MenuItem, Category
from decimal import Decimal
import bleach

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
    title = serializers.CharField( # METHOD 1 (Unique Validator): pass to field itself
        max_length=255,
        validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    )
    stock = serializers.IntegerField(source='inventory', min_value=1)
    calculated_tax = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=10) # METHOD 1 (Conditions): Adding condition to price field (cannot be less than 10.0)
    category = CategorySerializer(read_only=True) # to be able to perform post request in api/menu-items uncomment this line and comment below part
    # category = serializers.HyperlinkedRelatedField ( # This part creates a hyperlink refers to name='category-detail' named url. Instead of that, it could be done by passing (serializers.HyperlinkedModelSerializer) to "PASS HERE"
    #     queryset = Category.objects.all(),
    #     view_name='category-detail',
    # )
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock',  'calculated_tax', 'category']
        # depth=1 # same as (category = CategorySerializer()). This way you don't need the CategorySerializer
        # extra_kwargs = { # METHOD 2 (Conditions): Rather than defining and adding conditions to the field we can add conditions using (extra_kwargs)
        #     'price': {'min_value': 2}
        # }

        # METHOD 2 (Unique Validator): Define it in extra_kwargs
        # extra_kwargs = {
        #     'title': {
        #         'validators': [
        #             UniqueValidator(
        #                 queryset=MenuItem.objects.all()
        #             )
        #         ]
        #     }
        # }

        # Unique Validator Togather: You can define more than one field to validate unique values
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=MenuItem.objects.all(),
        #         fields=['title', 'price'],
        #     )
        # ]

    def get_calculated_tax(self, product:MenuItem):
        taxed_price = product.price * Decimal('1.10')
        return taxed_price.quantize(Decimal('0.00'))
    
    #METHOD 3 (Conditions): Defining conditions with function
    # def validate_price(self, value):
    #     if value < 10:
    #         return serializers.ValidationError('Price should not be less than 10.0')
    #     return value

    #METHOD 4 (Conditions): Defining conditions with function and attrs parameter | Sanitize title field
    # def validate(self, attrs):
    #     attrs['title'] = bleach.clean(attrs['title'])
    #     if(attrs['price']<2):
    #         raise serializers.ValidationError('Price should not be less than 2.0')
    #     if(attrs['inventory']<0):
    #         raise serializers.ValidationError('Stock cannot be negative')
    #     return super().validate(attrs)

    # Sanitizes user input by cleaning HTML tags and attributes to mitigate XSS (Cross-Site Scripting) attacks.
    """
    If we try to inject HTML here is the result:
    injected field    ->     title = Baklava <script>alert('Hello')</script> Dessert
    Output            ->    "title": "Baklava &lt;script&gt;alert('Hello')&lt;/script&gt; Dessert",

    """
    def validate_title(self, value):
        return bleach.clean(value)
