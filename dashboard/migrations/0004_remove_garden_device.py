# Generated by Django 3.1.3 on 2020-12-15 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20201215_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garden',
            name='device',
        ),
    ]
