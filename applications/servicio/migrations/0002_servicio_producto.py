# Generated by Django 3.1.4 on 2020-12-13 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='producto',
            field=models.ManyToManyField(to='producto.producto'),
        ),
    ]
