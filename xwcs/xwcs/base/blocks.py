
from django.db import models

from wagtail import blocks
from wagtail import admin

from xwcs.base.views import h5p_module_chooser_viewset

from xwcs.base.models import H5PModule

_H5PChooserBlock = h5p_module_chooser_viewset.get_block_class(name="H5PChooserBlock", module_path="xwcs.base.blocks") 

# doing this just so template can be added
class H5PChooserBlock(_H5PChooserBlock):
    class Meta:
        template = "h5p_module_template.html"