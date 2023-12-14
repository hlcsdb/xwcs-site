from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.documents.models import AbstractDocument


class H5PModuleFile(AbstractDocument):
    title = models.CharField("H5P module title", max_length=254)
    h5p_file = models.FileField(upload_to="documents", verbose_name=_("file"))

    admin_form_fields = ("title", "file", "collection", "tags")

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_h5p", "Can choose h5p module")
        ]

        verbose_name = _("h5p module")
        verbose_name_plural = _("h5p modules")

    # def clean(self):
    #     allowed_extensions = [".zip", ".h5p"]
    #     if allowed_extensions:
    #         validate = FileExtensionValidator(allowed_extensions)
    #         validate(self.file)

    @property
    def content_type(self):
        return "application/zip"