from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path(r'personajes', include('personajes.urls')),
    path(r'cuentas', include('accounts.urls')),

]
