# Generated by Django 2.2.2 on 2019-06-26 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190626_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='acad_state',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='acads',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='tags',
        ),
    ]
