# Generated by Django 2.2.13 on 2021-03-14 02:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectDescriptions',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]