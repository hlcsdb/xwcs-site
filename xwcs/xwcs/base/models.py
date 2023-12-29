from zipfile import ZipFile
from pathlib import Path

from django.db import models
from django.db.models.signals import post_init

from wagtail.admin.panels import FieldPanel

from wagtail.documents.models import Document, AbstractDocument

class H5PFile(AbstractDocument):
    file = models.FileField(upload_to="h5p", verbose_name="H5P file")

class H5PModule(models.Model):
    title = models.CharField(max_length=255)
    h5p_file = models.FileField(upload_to="h5p", verbose_name="H5P file", null=True, blank=True)
    # h5p_file = models.ForeignKey(H5PFile, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name=("created at"), auto_now_add=True)

    @property
    def h5p_json(self):
        extracted_h5p = self.extract_h5p()
        return Path(self.h5p_file.url).with_suffix("")

    def extract_h5p(self):
        h5p_extract_path = Path(self.h5p_file.path).with_suffix("")
        if not h5p_extract_path.is_dir():
            with ZipFile(self.h5p_file) as zf:
                zf.extractall(h5p_extract_path)
        
        return h5p_extract_path


    panels = [
        FieldPanel('title'),
        FieldPanel('h5p_file')
    ]

    class Meta:
        verbose_name = "H5P module"
        verbose_name_plural = "H5P modules"

    
    def __str__(self):
        return self.title
    