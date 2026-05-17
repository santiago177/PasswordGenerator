from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_generator_ui, name='password_generator_ui'),
    path('generate-password/', views.generate_password_view, name='generate_password'),
]

