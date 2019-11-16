from django.conf.urls import include, url

from django.urls import path
from . import views
app_name ='blog'
urlpatterns = [
    url(r'^$', views.main,name='home'),
    url(r'^listaPersonajes$', views.listaPersonajes,name='personajes'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path(r'^post/new/$', views.post_new, name='post_new'),
    


]
