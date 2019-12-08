# Generated by Django 2.2.7 on 2019-12-07 20:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buscar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('paterno', models.CharField(max_length=100)),
                ('materno', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=13, unique=True, validators=[django.core.validators.MinLengthValidator(13, 'Error de logitud')])),
                ('curp', models.CharField(max_length=18, unique=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('S', 'Soltero'), ('C', 'Casado')], max_length=1, null=True)),
                ('status', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('pais_nacimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_nacimiento', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('municipio_nacimiento', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('pais_residencia', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_residencia', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('municipio_residencia', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('localidad_reside', models.CharField(blank=True, max_length=100, null=True)),
                ('calle', models.CharField(blank=True, max_length=100, null=True)),
                ('colonia', models.CharField(blank=True, max_length=100, null=True)),
                ('cp', models.CharField(blank=True, max_length=6, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
