from rest_framework.routers import SimpleRouter
from measurements.views import ProjectViewSet, MeasurementViewSet


router = SimpleRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('measurement', MeasurementViewSet, basename='measurement')
urlpatterns = router.urls
