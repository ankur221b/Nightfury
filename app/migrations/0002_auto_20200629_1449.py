# Generated by Django 2.2.12 on 2020-06-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='form',
            name='imageurl',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
