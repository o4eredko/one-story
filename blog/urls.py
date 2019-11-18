from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
# router.register('auth', UserViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
	path('', include(router.urls))
]
