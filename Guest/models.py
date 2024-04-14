

from email.policy import default
from pyexpat import model
from Admin.models import *



# Create your models here.
class tbl_coach(models.Model):
     coach_name=models.CharField(max_length=20)
     coach_email=models.CharField(max_length=20)
     coach_contact=models.CharField(max_length=20)
     coach_gender=models.CharField(max_length=20)
     coach_dob=models.CharField(max_length=20)
     place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
     event=models.ForeignKey(tbl_event,on_delete=models.CASCADE,null=True)
     coach_address=models.CharField(max_length=50,null=True)
     coach_photo=models.FileField(upload_to='CoachDoc/')
     coach_licence=models.FileField(upload_to='Coachlic')
     coach_password=models.CharField(max_length=20)
     coach_vstatus=models.CharField(max_length=1,default="0",null=True)  




class tbl_shop(models.Model):
     shop_name=models.CharField(max_length=20)
     shop_email=models.CharField(max_length=20)
     shop_contact=models.CharField(max_length=20)
     shop_address=models.CharField(max_length=100)
     shop_photo=models.FileField(upload_to='Shopphoto/')
     shop_proof=models.FileField(upload_to='Shopproof/')
     place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
     shop_password=models.CharField(max_length=20)
     shop_vstatus=models.CharField(max_length=1,default="0")

class tbl_user(models.Model):
     user_name=models.CharField(max_length=20)
     user_email=models.CharField(max_length=20)
     user_contact=models.CharField(max_length=20)
     place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
     user_gender=models.CharField(max_length=20)
     user_address=models.CharField(max_length=500)
     user_dob=models.CharField(max_length=20)
     user_photo=models.FileField(upload_to='Userphoto/')
     user_proof=models.FileField(upload_to='Userproof/')
     user_password=models.CharField(max_length=20)
     user_vstatus=models.CharField(max_length=20,default="0",null=True)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    coach_from = models.ForeignKey(tbl_coach,on_delete=models.CASCADE,related_name="coach_from",null=True)
    coach_to = models.ForeignKey(tbl_coach,on_delete=models.CASCADE,related_name="coach_to",null=True)

class tbl_queries(models.Model):
     queries_name=models.CharField(max_length=20)
     queries_email=models.CharField(max_length=20)
     queries_message=models.CharField(max_length=500)
     



class complaint(models.Model):
     complaint_title=models.CharField(max_length=500)
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     coach=models.ForeignKey(tbl_coach,on_delete=models.CASCADE)
     shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
     complaint_content=models.CharField(max_length=500)
     comaplaint_replay=models.CharField(max_length=500)
     comaplaint_status=models.CharField(max_length=1)
     complaint_date=models.DateField()