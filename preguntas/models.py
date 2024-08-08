from django.db import models

from webFootball.settings import MEDIA_URL, STATIC_URL

class Section(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la seccion", blank=True, null=True)
    descrpcion = models.TextField(max_length=400, verbose_name="Descripcion de la seccion", blank=True, null=True)
    image = models.ImageField(upload_to='section-image/', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    def __str__(self):
        return self.nombre



class Category(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='categoy-image/', null=True, blank=True)
    descripcion = models.TextField(verbose_name="descripcion", blank=True, null=True, max_length=300)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    def __str__(self):
        return self.nombre

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
