from django.db import models
#from encrypted_model_fields.fields import EncryptedCharField

class Cash(models.Model):
    customer = models.CharField(max_length=150,null=False,blank=False)
    cash_model = models.CharField(max_length=50,null=False,blank=False)
    cash_number = models.CharField(max_length=50,null=False,blank=False)
    register_date = models.DateField(null=False,blank=False)
    old_os = models.CharField(max_length=50,null=True,blank=True)
    new_os = models.CharField(max_length=50,null=True,blank=True)
    status = models.BooleanField(default=True, blank=False,null=False)
    info = models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = 'Ταμειακές'
        verbose_name_plural = 'Ταμειακές'
        ordering = ['customer']
