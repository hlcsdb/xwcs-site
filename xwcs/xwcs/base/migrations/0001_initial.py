# Generated by Django 5.0 on 2023-12-28 00:36

import wagtail.documents.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='H5PModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('h5p_file', wagtail.fields.StreamField([('h5p_file', wagtail.documents.blocks.DocumentChooserBlock())], use_json_field=True)),
            ],
            options={
                'verbose_name': 'H5P module',
                'verbose_name_plural': 'H5P modules',
            },
        ),
    ]