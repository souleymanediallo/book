# Generated by Django 5.0.1 on 2024-01-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=50),
        ),
    ]
