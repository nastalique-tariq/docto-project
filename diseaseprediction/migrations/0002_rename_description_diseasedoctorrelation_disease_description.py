# Generated by Django 4.0.6 on 2022-07-24 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseaseprediction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseasedoctorrelation',
            old_name='description',
            new_name='disease_description',
        ),
    ]
