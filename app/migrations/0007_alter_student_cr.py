# Generated by Django 4.2.4 on 2023-08-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_went_student_went'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]