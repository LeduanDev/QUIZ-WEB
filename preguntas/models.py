
from django.db import models
import os
from webFootball.settings import MEDIA_URL, STATIC_URL, MEDIA_ROOT
from django.core.exceptions import ValidationError

from webFootball import settings

class Section(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la seccion", blank=True, null=True)
    descrpcion = models.TextField(max_length=400, verbose_name="Descripcion de la seccion", blank=True, null=True)
    image = models.ImageField(upload_to='section-image/', null=True, blank=True)
    icono = models.CharField(max_length=10, verbose_name="icono", blank=True, null=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    def __str__(self):
        return self.nombre


## Modelo para los quizzes, estos son los quizzes
class Category(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='categoy-image/', null=True, blank=True)
    descripcion = models.TextField(verbose_name="descripcion", blank=True, null=True, max_length=300)
    enable_timer = models.BooleanField(default=False) 
    difficulty =  models.CharField(max_length=30, null=True, blank=True)
    quiz_duration =  models.DurationField(null=True, blank=True)

    def clean(self):
        if self.quiz_duration and self.quiz_duration.total_seconds() <= 0:
            raise ValidationError("Quiz duration must be a positive number of seconds.")
        
        if self.enable_timer and not self.quiz_duration:
            raise ValidationError("You must set a quiz duration if the timer is enabled")

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    def __str__(self):
        return self.nombre


class CategoryimageSlider(models.Model):
    category = models.ForeignKey(Category, related_name="Imagenes", on_delete=models.CASCADE)
    images =  models.ImageField(upload_to="slider/",null=True, blank=True)

    def get_image(self):
        if self.images:
            return '{}{}'.format(MEDIA_URL, self.images)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    def delete(self, *args, **kwargs):
        # Verificar si existe la imagen antes de eliminar el objeto
        if self.images:
            # Construir la ruta absoluta del archivo
            image_path = os.path.join(settings.MEDIA_ROOT, self.images.name)
            # Eliminar la imagen si existe en el sistema de archivos
            if os.path.isfile(image_path):
                os.remove(image_path)
        # Llamar al método delete original para eliminar el objeto
        super().delete(*args, **kwargs)
    def __str__(self):
        return f"Imagen para {self.category.nombre}"


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    question_text = models.CharField(max_length=255)
    points = models.IntegerField(default=1)  # Añadir campo de puntaje

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
