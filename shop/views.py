from django.shortcuts import render
from rest_framework import filters
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import status
from .serializers import(
     TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer,
    UserSerializer,
    CategorySerialzier,
    BrandSerialzier,
    ProductSerializer,
    ReviewsSerializer,
    OrderItemSerializer,
    OrderSerializer,
    ShippingAddressSerializer,
)
from . models import (
    ShippingAddress,
    Product,
    Order,
    OrderItem,
    ShopUser,
    Review,
    Brand,
    Category
)
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets,permissions,parsers




class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  ShopUser.objects.all()
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    throttle_scope = 'users'

    @extend_schema(tags=['Auth'],summary='create new user account')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='get all account')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='retireve user account')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='update user account')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='partial user account')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='delete user account')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    



class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset =  Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser,parsers.FormParser]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['category', 'in_stock']
    search_fields = ['name', 'color']
    throttle_scope = 'product'

    @extend_schema(tags=['Product'],summary='create new product',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Product'],summary='get all product')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Product'],summary='retrieve product by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Product'],summary='update product')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Product'],summary='partial update product')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Product'],summary='delete product')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerialzier
    queryset =  Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    throttle_scope = 'categories'

    @extend_schema(tags=['Category'],summary='create new category',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='get all categories')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='retrieve category by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='update category')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='partial update category')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='delete category')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerialzier
    queryset =  Brand.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = 'brand'

    @extend_schema(tags=['Brand'],summary='create new brand',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Brand'],summary='get all brands')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Brand'],summary='retrieve brand by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Brand'],summary='update brand')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Brand'],summary='partial update brand')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Brand'],summary='delete brand')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class ShippingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingAddressSerializer
    queryset = ShippingAddress.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['city','state','address']

    @extend_schema(tags=['ShippingAddress'],summary='create new shipping address',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['ShippingAddress'],summary='get all shippingAddress')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['ShippingAddress'],summary='retrieves hipping address by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['ShippingAddress'],summary='update shipping address')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['ShippingAddress'],summary='partial update shipping address')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['ShippingAddress'],summary='delete shipping address')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset =  Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=['Order'],summary='create new order',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=['Order'],summary='get all orders')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Order'],summary='retrieves order by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Order'],summary='update shipping order')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Order'],summary='partial update shipping order')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Order'],summary='delete order')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset =  OrderItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=['OrderItem'],summary='create new order_item',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['OrderItem'],summary='get all orderItems')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['OrderItem'],summary='retrieves order_item by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['OrderItem'],summary='update order_item')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['OrderItem'],summary='partial update order_item')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['OrderItem'],summary='delete order_item')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer,
    queryset =  Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=['Review'],summary='create new review',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Review'],summary='get all reviews')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Review'],summary='retrieves review by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Review'],summary='update shipping review')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Review'],summary='partial update review')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Review'],summary='delete review')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @extend_schema(tags=['Auth'],summary='get token',
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class DecoratedTokenRefreshView(TokenRefreshView):
    @extend_schema(tags=['Auth'],summary='refresh token',
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)