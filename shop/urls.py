from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers 
from . import views

router = routers.SimpleRouter()
router.register(r'users',views.UserViewSet)
router.register(r'products',views.ProductViewSet)
router.register(r'brands',views.BrandViewSet)
router.register(r'categories',views.CategoryViewSet)
router.register(r'orders',views.OrderViewSet)
router.register(r'orderItems',views.OrderItemViewSet)
router.register(r'shippingaddress',views.ShippingAddressViewSet)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/',views.DecoratedTokenObtainPairView.as_view(),name="token"),
    path('api/token/refresh/',views.DecoratedTokenRefreshView.as_view(),name="refresh_token"),
]
urlpatterns += router.urls
