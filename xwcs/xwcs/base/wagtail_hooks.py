from wagtail import hooks
from wagtail.admin.panels import (
    FieldPanel,
    MultipleChooserPanel,

)
from wagtail.snippets.models import register_snippet

from xwcs.base.models import H5PModule
from xwcs.base.views import h5p_module_chooser_viewset

@hooks.register("register_admin_viewset")
def register_viewset():
    return [
        h5p_module_chooser_viewset
    ]

register_viewset()

