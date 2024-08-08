from preguntas import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.home_view, name='home'),
     path('<int:category_id>/', views.quiz_view, name='quiz_view_by_category'),
     path('seccion/<int:seccion_id>/', views.categoriasSeccion, name='categorias'),
     path('carrousel', views.carousel, name='carousel')

]
