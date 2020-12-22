# Generated by Django 3.1.3 on 2020-12-22 04:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tipo_prod', models.CharField(max_length=10, verbose_name='Tipo')),
                ('description', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ingredientes', models.TextField()),
                ('preparacion', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(null=True, upload_to='recetas')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
    ]
