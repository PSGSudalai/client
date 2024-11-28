from apps.ADMIN.models.project import Project
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

class Document(BaseModel):
    doc_id = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    qua_id = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    
 
    def save(self, *args, **kwargs):
        # Generate doc_id if not already set
        if not self.doc_id:
            last_document = Document.objects.exclude(doc_id__isnull=True).order_by("id").last()
            if last_document and last_document.doc_id.startswith("DOC"):
                last_document_id = last_document.doc_id
                document_number = int(last_document_id.split("DOC")[-1]) + 1
                self.doc_id = f"DOC{document_number:04d}"
            else:
                self.doc_id = "DOC0001"

        # Generate qua_id if not already set
        if not self.qua_id:
            last_quotation = Document.objects.exclude(qua_id__isnull=True).order_by("id").last()
            if last_quotation and last_quotation.qua_id.startswith("QUO"):
                last_quotation_id = last_quotation.qua_id
                quotation_number = int(last_quotation_id.split("QUO")[-1]) + 1
                self.qua_id = f"QUO{quotation_number:04d}"
            else:
                self.qua_id = "QUO0001"

        super(Document, self).save(*args, **kwargs)