# Generated by Django 5.0 on 2023-12-28 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_h5pmodule_collection_remove_h5pmodule_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='h5pmodule',
            name='h5p_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.h5pfile'),
        ),
    ]
