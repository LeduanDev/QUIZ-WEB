# Generated by Django 5.0.6 on 2024-07-19 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0005_alter_category_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre de la seccion')),
                ('descrpcion', models.TextField(blank=True, max_length=400, null=True, verbose_name='Descripcion de la seccion')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preguntas.section'),
        ),
    ]
