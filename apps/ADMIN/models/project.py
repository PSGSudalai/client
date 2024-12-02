from apps.ADMIN.models import Client
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models




class Project(BaseModel):
    project_client= models.ForeignKey(Client,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    project_name =models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    team_leader =models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    task_no =models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    total_budget =models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    start_date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    deadline = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    description = models.TextField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)



  
