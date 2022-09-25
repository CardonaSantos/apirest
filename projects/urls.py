
from rest_framework import routers
from .api import ProjectViewSet

router=routers.DefaultRouter()#llamamos un router especial que es un modulo, y tambien lo ejecutamos, para luego meterlo en una variable y usarla para nosotros crear nuestras rutas
router.register('api/projects',ProjectViewSet, 'projects' )#va a estar basado en el conjunto de datos que vienen de: ProjectViewSet que tambien importamos arriba

urlpatterns = router.urls


