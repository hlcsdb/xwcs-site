# Generated by Django 5.0 on 2023-12-28 02:03

import django.db.models.deletion
import django.utils.timezone
import taggit.managers
import wagtail.models.collections
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('taggit', '0005_auto_20220424_2025'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('wagtaildocs', '0012_uploadeddocument'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='H5PModuleFile',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtaildocs.document')),
                ('h5p_file_upload', models.FileField(upload_to='h5p', verbose_name='h5p file')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
                'abstract': False,
            },
            bases=('wagtaildocs.document',),
        ),
        migrations.AddField(
            model_name='h5pmodule',
            name='collection',
            field=models.ForeignKey(default=wagtail.models.collections.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.collection', verbose_name='collection'),
        ),
        migrations.AddField(
            model_name='h5pmodule',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='h5pmodule',
            name='file',
            field=models.FileField(default='null', upload_to='documents', verbose_name='file'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='h5pmodule',
            name='file_hash',
            field=models.CharField(blank=True, editable=False, max_length=40),
        ),
        migrations.AddField(
            model_name='h5pmodule',
            name='file_size',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='h5pmodule',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='h5pmodule',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user'),
        ),
        migrations.AlterField(
            model_name='h5pmodule',
            name='h5p_file',
            field=models.FileField(upload_to='documents', verbose_name='H5P module'),
        ),
    ]
