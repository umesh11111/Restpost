from django.urls import path
from . import views

urlpatterns = [
    path('', views.getrequest, name='getR'),
    path('', views.postrequest, name='postR')

]