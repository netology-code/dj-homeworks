# Generated by Django 4.1.2 on 2023-02-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
