import uuid
from django.db import models
from django.urls import reverse
from encrypted_model_fields.fields import EncryptedCharField
from datetime import datetime
from .validators import validate_file_extension


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Cash(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.CharField(max_length=150,null=False,blank=False)
    cash_model = models.CharField(max_length=50,null=False,blank=False)
    cash_number = models.CharField(max_length=50,null=False,blank=False)
    register_date = models.DateField(null=True,blank=True)
    old_os = models.CharField(max_length=50,null=True,blank=True)
    new_os = models.CharField(max_length=50,null=True,blank=True)
    update_date = models.DateField(null=True,blank=True)
    aes_key = EncryptedCharField(max_length=150,null=True, blank=True)
    status = models.BooleanField(default=True, blank=True,null=True)
    info = models.TextField(blank=True,null=True)

    
    class Meta:
        verbose_name = 'Ταμειακές'
        verbose_name_plural = 'Ταμειακές'
        ordering = ['customer']

    def __str__(self):
        return str(self.customer)

def cash_directory_path(instance, filename):
    return 'cash_{0}/{1}'.format(instance.customer, filename)

class UploadFile(TimeStampMixin):
    customer = models.CharField(max_length=150,null=False,blank=False)
    file = models.FileField(upload_to=cash_directory_path,validators=[validate_file_extension])

    class Meta:
        verbose_name = 'Αρχεία'
        verbose_name_plural = 'Αρχεία'
        db_table = 'CashFiles'