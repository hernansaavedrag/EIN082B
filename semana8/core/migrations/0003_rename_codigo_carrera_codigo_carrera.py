# Generated by Django 5.0.4 on 2024-05-06 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_carrera_id_alter_carrera_codigo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrera',
            old_name='codigo',
            new_name='codigo_carrera',
        ),
    ]
