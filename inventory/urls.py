from rest_framework.routers import DefaultRouter

from .views import (
    CustomerViewSet,
    CategoryViewSet,
    ProductViewSet,
)


router = DefaultRouter()

router.register(
    'customers',
    CustomerViewSet,
    basename='customer'
)

router.register(
    'categories',
    CategoryViewSet,
    basename='category'
)

router.register(
    'products',
    ProductViewSet,
    basename='product'
)

urlpatterns = router.urls