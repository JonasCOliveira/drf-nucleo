# Generated by Django 4.0.4 on 2022-05-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_lat_descargas_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alvo',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='alvo',
            name='lng',
        ),
        migrations.AddField(
            model_name='alvo',
            name='coordenadas',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='alvo',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
    ]
