# Generated by Django 4.2.4 on 2023-08-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='firstShift',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='secondShift',
            field=models.BooleanField(default=False),
        ),
    ]
