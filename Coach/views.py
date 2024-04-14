

from urllib import request
from django.shortcuts import render,redirect

from Guest.models import *
from Coach.models import *
from User.models import *
from .models import *
from django.db.models import Q
from datetime import datetime

# Create your views here.
def CoachHP(request):
    coach = tbl_coach.objects.get(id=request.session["cid"])
    if request.method=="POST":
        return render(request,"Coach/CoachHP.html")
    else:
        return render(request,"Coach/CoachHP.html",{"data":coach})

def ViewCoach(request):
    coach = tbl_coach.objects.get(id=request.session["cid"])
    if request.method=="POST":
        return render(request,"Coach/Viewprofile.html"),
    else:
        return render(request,"Coach/Viewprofile.html",{"data": coach})
    
def EditCoach(request):
    coach=tbl_coach.objects.get(id=request.session["cid"])
    if request.method=="POST":
        coach.coach_name=request.POST.get("txt_name")
        coach.coach_contact=request.POST.get("txt_contact")
        coach.coach_address=request.POST.get("txt_address")
        coach.save()
        return redirect("webcoach:ViewCoach")
    else:
        return render(request,"Coach/EditProfile.html",{"data":coach})
    

def EPCoach(request):
    if request.method=="POST":
        coach=tbl_coach.objects.get(id=request.session['cid'])
        opassword=request.POST.get("txt_opassword")
        npassword=request.POST.get("txt_npassword")
        cpassword=request.POST.get("txt_cpassword")
        if coach.coach_password==opassword:
            if npassword == cpassword:
                coach.coach_password=request.POST.get("txt_npassword")
                coach.save()
                return redirect("webcoach:ViewCoach")
            else:
                msg="password missmatch !"
                return render(request,"Coach/Changepassword.html",{'msg':msg})
        else:
            msg="password missmatch !"
            return render(request,"Coach/Changepassword.html",{'msg':msg})
    else:
        return render(request,"Coach/Changepassword.html")



def Trainingdetails(request):
    event=tbl_event.objects.all()
    training=tbl_trainig.objects.all()
    if request.method == "POST":
        coach = tbl_coach.objects.get(id=request.session['cid'])
        eventdata = tbl_event.objects.get(id=request.POST.get("txt_event"),)
        tbl_trainig.objects.create(coach=coach,
                                 event = eventdata,
                                 training_duration=request.POST.get("txt_duration"),
                                 training_details=request.POST.get("txt_details"),
                                 
                                )   
        return render(request,"Coach/Trainingdetails.html",{"data":event,"tdata":training})
    else:
        return render(request,"Coach/Trainingdetails.html",{"data":event,"tdata":training})  
    

    

def AddSubscription(request):
    subscription=tbl_subscription.objects.all()
    if request.method=="POST":
        tbl_subscription.objects.create(subscription_amount=request.POST.get("txt_amount"),
                                     subscription_details=request.POST.get("txt_details"),
                                     )
        return render(request,"Coach/Addsubscription.html",{"data":subscription})
    else:
        return render(request,"Coach/Addsubscription.html",{"data":subscription})
    

def DailyPlan(request,id):
    dailyplan=tbl_dailyplan.objects.all()

    if request.method=="POST":
        training = tbl_trainig.objects.get(id=id)
        tbl_dailyplan.objects.create(training=training,
                                     dailyplan_day=request.POST.get("txt_day"),
                                     dailyplan_wcount=request.POST.get("txt_workout"),
                                     )
        return render(request,"Coach/DailyPlan.html",{"data":dailyplan})
    else:
        return render(request,"Coach/DailyPlan.html",{"data":dailyplan})
    



def Workout(request,id):
    workout=tbl_workout.objects.all()
    workoutcount=tbl_workout.objects.filter(dailyplan=id).count()
    dite = tbl_dailyplan.objects.get(id=id)
    ditecount = dite.dailyplan_wcount
    if workoutcount >= int(ditecount):
        return render(request,"Coach/Workout.html",{"data":workout,"alt":1})
    else:
        if request.method=="POST":
            dailyplan=tbl_dailyplan.objects.get(id=id)
            tbl_workout.objects.create(dailyplan=dailyplan,
                                    workout_name=request.POST.get("txt_name"),
                                    workout_discription=request.POST.get("txt_discription"),
                                    workout_file=request.FILES.get("txt_file"),
                                    )
            return render(request,"Coach/Workout.html",{"msg":"Data Added..","ID":id})
        else:
            return render(request,"Coach/Workout.html",{"data":workout})
        


def Followers(request):
    follower = tbl_follow.objects.filter(coach=request.session["cid"])
    return render(request,"Coach/Followers.html",{"data":follower})

def chatpage(request,id):
    foll = tbl_follow.objects.get(id=id)
    user  = tbl_user.objects.get(id=foll.user_id)
    print(user.user_name)
    return render(request,"Coach/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_coach.objects.get(id=request.session["cid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),coach_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Coach/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_coach.objects.get(id=request.session["cid"])
    chat_data = tbl_chat.objects.filter((Q(coach_from=user) | Q(coach_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Coach/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(coach_from=request.session["cid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(coach_to=request.session["cid"]))).delete()
    return render(request,"Coach/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})