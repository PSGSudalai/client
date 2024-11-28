from apps.BASE.model_fields import AppSingleChoiceField, AppSingleFileField
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

from apps.HELPERS.choices import STATUS

class ProjectImage(BaseModel):
    file =AppSingleFileField(upload_to="files/project/images")

class Project(BaseModel):
    title =models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    status = AppSingleChoiceField(choices_config = STATUS,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    image = models.ForeignKey(ProjectImage,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    amount =models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    start_date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    end_date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)


    def __str__(self):
        return self.title
