# Generated by Django 3.0.2 on 2020-04-10 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tutor',
        ),
        migrations.RenameField(
            model_name='tutee',
            old_name='timesTutteed',
            new_name='timesTuteed',
        ),
    ]