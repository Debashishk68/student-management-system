# Generated by Django 5.2 on 2025-06-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
