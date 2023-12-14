from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.search import index

class LessonIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = ['lessons.LessonPage']

class LessonPage(Page):
    # Lesson text

    date = models.DateField("Updated date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock())],
        use_json_field=True
    )        
    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    # Content panels

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
    ]

    parent_page_types = ['lessons.LessonIndexPage']