# Generated by Django 4.0.5 on 2022-06-15 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_categoria_delete_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('rol', models.CharField(max_length=15)),
                ('rut', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='item',
            name='usuario',
        ),
        migrations.CreateModel(
            name='prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateTimeField(blank=True, null=True, verbose_name='fecha prestamo')),
                ('fecha_devuelto', models.DateTimeField(blank=True, null=True, verbose_name='fecha devuelto')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.categoria'),
        ),
    ]
