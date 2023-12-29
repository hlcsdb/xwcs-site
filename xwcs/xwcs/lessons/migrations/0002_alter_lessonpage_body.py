# Generated by Django 5.0 on 2023-12-28 02:41

import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks
import xwcs.base.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('h5p_module', wagtail.blocks.StructBlock([('h5p_file', wagtail.snippets.blocks.SnippetChooserBlock(xwcs.base.models.H5PModule))]))], use_json_field=True),
        ),
    ]
