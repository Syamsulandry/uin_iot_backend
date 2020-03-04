from rest_framework import routers
from detektor_suhu.views import StatsViewset

router = routers.DefaultRouter()
router.register('stats', StatsViewset)

urlpatterns = []
urlpatterns += router.urls