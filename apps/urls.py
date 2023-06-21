from django.contrib import admin
from django.urls import path,include
from .import views
# serializers
from .views import StudentViewSet
from rest_framework import routers





'''urlpatterns = [
    path('',views.index)
]'''
router=routers.DefaultRouter()
router.register(r'students',StudentViewSet)


urlpatterns = [
    #path('',views.index),
    path('',include(router.urls))
]