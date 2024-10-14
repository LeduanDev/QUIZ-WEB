from preguntas import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.home_view, name='home'),
     path('quizz/take/<int:category_id>/', views.quiz_view, name='take_quizz'),
     path('seccion/<int:seccion_id>/', views.categoriasSeccion, name='categorias'),
     path('secciones', views.allSection, name='allsections'),
     path('detalles/<int:categorie_id>/', views.details, name='details')

]
