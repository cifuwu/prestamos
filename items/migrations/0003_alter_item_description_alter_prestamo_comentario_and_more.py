# Generated by Django 4.0.4 on 2022-06-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_categoria_alter_item_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='comentario',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devuelto',
            field=models.DateTimeField(blank=True, verbose_name='fecha devuelto'),
        ),
    ]
