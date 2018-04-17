from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
#    path('$/', views.products, name='products'),
#    path('$/', views.comments, name='comments'),
    path('', views.index, name='index'),
    path('', views.home, name='home')
]
