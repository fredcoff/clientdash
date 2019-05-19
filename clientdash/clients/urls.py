from rest_framework import routers
from .api import ClientViewSet

router = routers.DefaultRouter()
router.register('', ClientViewSet, 'clients')

urlpatterns = router.urls