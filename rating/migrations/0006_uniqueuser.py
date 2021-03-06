# Generated by Django 2.2.4 on 2019-11-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20191105_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(null=True, unique=True, unpack_ipv4=True)),
                ('deputies', models.ManyToManyField(to='rating.Deputy')),
            ],
        ),
    ]
