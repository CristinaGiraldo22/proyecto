#definir las rutas de un app web
# from django.urls import path, include

# from api import views

# urlpatterns = [
#     path('', views.index, name="index"),
# ]

# crear una ruta con django rest framework  

from rest_framework import routers
from .api import ApiViewSet

ruta = routers.DefaultRouter()
ruta.register('api/Employee',ApiViewSet,'api')

urlpatterns = ruta.urls


