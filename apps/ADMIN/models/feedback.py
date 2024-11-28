from apps.ACCESS.models import User
from apps.ADMIN.models import Document
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, BaseModel
from django.db import models

class Feedback(BaseModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    document = models.ForeignKey(Document,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    description = models.TextField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)