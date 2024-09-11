from rest_framework.routers import DefaultRouter
from .views import DonateurViewSet, HopitalViewSet, MedecinViewSet, ReceveurViewSet, PocheViewSet

router = DefaultRouter()
router.register(r'donateurs', DonateurViewSet)
router.register(r'hopitaux', HopitalViewSet)
router.register(r'medecins', MedecinViewSet)
router.register(r'receveurs', ReceveurViewSet)
router.register(r'poches', PocheViewSet)

urlpatterns = router.urls
