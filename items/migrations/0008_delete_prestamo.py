# Generated by Django 4.0.5 on 2022-06-15 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_categoria_usuario_remove_item_comentario_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='prestamo',
        ),
    ]
