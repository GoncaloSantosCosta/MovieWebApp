# Generated by Django 4.1.3 on 2022-12-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brDbproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]