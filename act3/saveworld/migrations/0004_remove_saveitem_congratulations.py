# Generated by Django 2.1 on 2020-09-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saveworld', '0003_savior'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saveitem',
            name='congratulations',
        ),
    ]