# Generated by Django 4.0.6 on 2022-07-24 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseaseprediction', '0007_alter_diseasedoctorrelation_disease_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseasedoctorrelation',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='diseasedoctorrelation',
            name='disease_description',
        ),
        migrations.RemoveField(
            model_name='diseasedoctorrelation',
            name='doctor',
        ),
    ]
