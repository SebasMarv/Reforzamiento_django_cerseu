# Generated by Django 4.1.6 on 2023-03-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='generacion',
            field=models.CharField(default='NaN', max_length=10),
        ),
    ]
