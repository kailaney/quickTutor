# Generated by Django 3.0.2 on 2020-04-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]