from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class tbl_state(models.Model):
    state_name=models.CharField(max_length=20)
        
class tbl_district(models.Model):
    district_name=models.CharField(max_length=20)
    state=models.ForeignKey(tbl_state,on_delete=models.CASCADE)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=20)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=20)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_scategory(models.Model):
    scategory_name=models.CharField(max_length=20)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_event(models.Model):
    event_name=models.CharField(max_length=20)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=20)
    admin_email=models.CharField(max_length=20)
    admin_contact=models.CharField(max_length=20)
    admin_password=models.CharField(max_length=20)