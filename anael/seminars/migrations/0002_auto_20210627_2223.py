# Generated by Django 3.2.4 on 2021-06-27 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('-city_name',)},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ('-region_name',)},
        ),
        migrations.RenameField(
            model_name='city',
            old_name='city_nme',
            new_name='city_name',
        ),
    ]
