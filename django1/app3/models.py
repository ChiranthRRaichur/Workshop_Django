from django.db import models

# Create your models here.
class Customers(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    adhaar_num = models.CharField(max_length=12)
    cust_id=models.AutoField(primary_key=True)
   
    def __str__(self):
        return self.firstname
