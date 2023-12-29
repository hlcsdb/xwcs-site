from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.admin.viewsets.base import ViewSet, ViewSetGroup
from xwcs.base.models import H5PModule, H5PFile

class H5PModuleChooserViewSet(ChooserViewSet):
    model = H5PModule
    upload_file_text = "Upload H5P file"
    choose_file_text = "Choose H5P file"
    form_fields = ["title", "h5p_file"]
    add_to_admin_menu = True

h5p_module_chooser_viewset = H5PModuleChooserViewSet("h5p_module_chooser")