# Generated by Django 3.0.2 on 2020-04-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200404_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asker',
            field=models.CharField(default='', max_length=5),
        ),
    ]