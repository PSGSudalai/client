from apps.ADMIN.models import Project
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

class Task(BaseModel):
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    task_name = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    start_date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    end_date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    hour = models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
