# Generated by Django 5.0.6 on 2024-07-30 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_inmueble_imagen1_inmueble_imagen2_inmueble_imagen3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='imagen1',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='imagen2',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='imagen3',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
