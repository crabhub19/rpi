# Generated by Django 4.2.4 on 2023-08-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_instructor_firstshift_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='firstShift',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='secondShift',
            field=models.BooleanField(default=False, null=True),
        ),
    ]