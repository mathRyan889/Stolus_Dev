from django.contrib import admin
from django.urls import path
from MeuSite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
]
