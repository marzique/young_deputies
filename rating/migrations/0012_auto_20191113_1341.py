# Generated by Django 2.2.4 on 2019-11-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0011_deputy_name_ukr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deputy',
            old_name='rating_upfoundation',
            new_name='upr',
        ),
        migrations.RemoveField(
            model_name='deputy',
            name='attendance',
        ),
        migrations.AddField(
            model_name='deputy',
            name='experts',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]