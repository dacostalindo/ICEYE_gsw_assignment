# Generated by Django 2.1 on 2020-09-07 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saveworld', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveitem',
            name='congratulations',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
