# Generated by Django 3.2.6 on 2021-08-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelnewapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='img',
            field=models.ImageField(upload_to='picturess'),
        ),
    ]
