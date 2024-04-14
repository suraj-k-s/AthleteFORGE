from unittest.util import _MAX_LENGTH
from django.db import models
from Admin.models import tbl_event
from Guest.models import tbl_coach
# Create your models here.


class tbl_trainig(models.Model):
    event=models.ForeignKey(tbl_event,on_delete=models.CASCADE)
    coach=models.ForeignKey(tbl_coach,on_delete=models.CASCADE)
    training_duration=models.CharField(max_length=20)
    training_details=models.CharField(max_length=500)

class tbl_subscription(models.Model):
    subscription_amount=models.CharField(max_length=20)
    subscription_details=models.CharField(max_length=500)
    coach = models.ForeignKey(tbl_coach,on_delete=models.SET_NULL,null=True)
    

class tbl_dailyplan(models.Model):
    training=models.ForeignKey(tbl_trainig,on_delete=models.CASCADE)
    dailyplan_day=models.CharField(max_length=20)
    dailyplan_wcount=models.CharField(max_length=20)


class tbl_workout(models.Model):
    dailyplan=models.ForeignKey(tbl_dailyplan,on_delete=models.CASCADE)
    workout_name=models.CharField(max_length=20)
    workout_discription=models.CharField(max_length=500)
    workout_file=models.FileField(upload_to='workout-file/')