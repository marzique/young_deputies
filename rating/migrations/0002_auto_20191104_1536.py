# Generated by Django 2.2.4 on 2019-11-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deputy',
            name='photo',
            field=models.CharField(max_length=200),
        ),
    ]
