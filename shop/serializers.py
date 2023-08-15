from rest_framework import serializers
from . models import (
    ShopUser,
    Product,
    Order,
    OrderItem,
    Review,
    Category,
    Brand,
    ShippingAddress
    )


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price','description','stock_quantity','image','category','brand','size','color','created_at','in_stock','reviews']

class CategorySerialzier(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['name','products']


class BrandSerialzier(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ['name','products']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields =['id','products','customer','ordered_date','status','total_amount','orderitem']
   

class ShippingAddressSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True,read_only=True)
    class Meta:
        model = ShippingAddress
        fields = ['owner','address','item','city','state','country','orders']


class UserSerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddressSerializer(many=True,read_only=True)
    orders = OrderSerializer(many=True,read_only=True)
    class Meta:
        model = ShopUser
        fields = ['email','password','shipping_address','orders']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = ShopUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user





























class UserSerialzier(serializers.ModelSerializer):
   #product = ArticleSerializer(many=True, read_only=True)
   
   class Meta:
        model = ShopUser
        fields = ['email','password','articles']
        extra_kwargs = {'password': {'write_only': True}}

   def create(self, validated_data):
        user = ShopUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




## token sserializers

class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
    


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()   