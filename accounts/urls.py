from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, UserViewSet

router = DefaultRouter()

router.register('companies', CompanyViewSet, basename='company')
router.register('users', UserViewSet, basename='user')

urlpatterns = router.urls