# Generated by Django 5.0 on 2023-12-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_h5pmodule_h5p_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='h5pmodule',
            name='h5p_file',
            field=models.FileField(upload_to='h5p', verbose_name='H5P file'),
        ),
    ]
