# Generated by Django 2.2.13 on 2021-03-14 02:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210314_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectDescriptions',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]