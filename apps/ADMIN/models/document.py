from apps.BASE.model_fields import AppSingleChoiceField, AppSingleFileField
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

from apps.HELPERS.choices import ACKNOWLEDGEMENT


class DocumentFile(BaseModel):
    file = AppSingleFileField(upload_to="files/document/images")

class DocumentFeedback(BaseModel):
    description = models.TextField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)


class Document(BaseModel):
    image = models.ForeignKey(DocumentFile,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    document_id = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    acknowledgement = AppSingleChoiceField(choices_config=ACKNOWLEDGEMENT,default='Waiting for Approval')
    feedback = models.ForeignKey(DocumentFeedback,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    


    