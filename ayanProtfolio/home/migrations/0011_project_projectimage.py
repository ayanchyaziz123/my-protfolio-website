# Generated by Django 3.1.7 on 2021-03-28 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210325_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
