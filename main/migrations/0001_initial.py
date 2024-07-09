# Generated by Django 5.0.6 on 2024-07-09 01:41

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=1500)),
                ('m2_construidos', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('m2_totales_terreno', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cantidad_estacionamientos', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cantidad_habitaciones', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('cantidad_baños', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000)])),
                ('direccion', models.CharField(max_length=255)),
                ('tipo_inmueble', models.CharField(choices=[('casa', 'Casa'), ('parcela', 'Parcela'), ('departamento', 'Departamento')], max_length=255)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmuebles', to='main.comuna')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmuebles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
