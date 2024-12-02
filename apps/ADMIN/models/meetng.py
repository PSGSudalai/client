from apps.ADMIN.models import Project
from apps.BASE.model_fields import AppSingleChoiceField
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

from apps.HELPERS.choices import STATUS

class Meeting(BaseModel):
    project_meeting = models.ForeignKey(Project,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    title = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    start_time = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    end_time = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    duration = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,*DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    team = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    link = models.URLField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    status = AppSingleChoiceField(choices_config=STATUS,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    description = models.TextField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)

    