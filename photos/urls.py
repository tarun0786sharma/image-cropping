from django.urls import path

from . import views

urlpatterns = [
    path('', views.add, name='image_add'),
    path('/', views.add, name='image_add')
]