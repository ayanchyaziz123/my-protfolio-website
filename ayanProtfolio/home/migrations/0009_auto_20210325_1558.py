# Generated by Django 3.1.7 on 2021-03-25 09:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_project_projectbody'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectBody',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]