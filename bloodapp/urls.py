from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Admin
    path('login/', views.admin_login, name='login'),

    # User page
    path('', views.index, name='index'),
]