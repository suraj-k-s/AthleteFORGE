from ctypes.wintypes import POINT
import re
from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import tbl_coach, tbl_queries, tbl_shop, tbl_user

# Create your views here.

def Coach(request):
    state=tbl_state.objects.all()
    district=tbl_district.objects.all()
    event=tbl_event.objects.all()
    if request.method == "POST":
        eventdata=tbl_event.objects.get(id=request.POST.get("txt_event"))
        place = tbl_place.objects.get(id=request.POST.get("txt_place"),)
        tbl_coach.objects.create(coach_name=request.POST.get("txt_name"),
                                 coach_email=request.POST.get("txt_email"),
                                 coach_contact=request.POST.get("txt_contact"),
                                 coach_address=request.POST.get("txt_address"),
                                 coach_gender=request.POST.get("txt_gender"),
                                 coach_dob=request.POST.get("txt_dob"),
                                 place=place,
                                 event=eventdata,
                                 coach_photo=request.FILES.get("txt_photo"),
                                 coach_licence=request.FILES.get("txt_licence"),
                                 coach_password=request.POST.get("txt_password")
                                )   
        return render(request,"Guest/coachregistration.html",{"disdata":district,"sdata":state,"edata":event})
    else:
        return render(request,"Guest/coachregistration.html",{"disdata":district,"sdata":state,"edata":event})
def Ajaxdistrict(request):
    sdata=tbl_state.objects.get(id=request.GET.get("stateid"))
    disdata=tbl_district.objects.filter(state=sdata)
    return render(request,"Guest/AjaxDistrict.html",{"district":disdata})
def Ajaxplace(request):
    disdata=tbl_district.objects.get(id=request.GET.get("distid"))
    placedata=tbl_place.objects.filter(district=disdata)
    return render(request,"Guest/AjaxPlace.html",{"Place":placedata})


def Shop(request):
    state=tbl_state.objects.all()
    district=tbl_district.objects.all()
    if request.method == "POST":
        place = tbl_place.objects.get(id=request.POST.get("txt_place"),)
        tbl_shop.objects.create(shop_name=request.POST.get("txt_name"),
                                 shop_email=request.POST.get("txt_email"),
                                 shop_contact=request.POST.get("txt_contact"),
                                 shop_address=request.POST.get("txt_address"),
                                 place=place,
                                 shop_photo=request.FILES.get("txt_photo"),
                                 shop_proof=request.FILES.get("txt_proof"),
                                 shop_password=request.POST.get("txt_password"),
                                )   
        return render(request,"Guest/shopregistration.html",{"disdata":district,"sdata":state})
    else:
        return render(request,"Guest/shopregistration.html",{"disdata":district,"sdata":state})




def User(request):
    state=tbl_state.objects.all()
    district=tbl_district.objects.all()
    if request.method == "POST":
        place = tbl_place.objects.get(id=request.POST.get("txt_place"),)
        tbl_user.objects.create( user_name=request.POST.get("txt_name"),
                                 user_email=request.POST.get("txt_email"),
                                 user_contact=request.POST.get("txt_contact"),
                                 place=place,
                                 user_gender=request.POST.get("txt_gender"),
                                 user_address=request.POST.get("txt_address"),
                                 user_dob=request.POST.get("txt_dob"),
                                 user_photo=request.FILES.get("txt_photo"),
                                 user_proof=request.FILES.get("txt_proof"),
                                 user_password=request.POST.get("txt_password"),
                                )   
        return render(request,"Guest/userregistration.html",{"disdata":district,"sdata":state})
    else:
        return render(request,"Guest/userregistration.html",{"disdata":district,"sdata":state})


def Login(request):
    if request.method=="POST":
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")
        coachcount=tbl_coach.objects.filter(coach_email=Email,coach_password=Password).count()
        admincount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()
        shopcount=tbl_shop.objects.filter(shop_email=Email,shop_password=Password).count()
        usercount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()

        if coachcount>0:
            coach = tbl_coach.objects.get(coach_email=Email,coach_password=Password)
            if coach.coach_vstatus=='0':
                return render(request,"Guest/login.html",{'msg':"Rgistration Pending"})
            elif coach.coach_vstatus=='2':
                return render(request,"Guest/login.html",{'msg':"Admin Rejected"})
            else:
                request.session["cid"] = coach.id
                return redirect("webcoach:CoachHP")
        elif usercount>0:
            user=tbl_user.objects.get(user_email=Email,user_password=Password)
            if user.user_vstatus=='0':
                return render(request,"Guest/login.html",{'msg':"Registration Pending"})
            elif user.user_vstatus=='2':
                return render(request,"Guest/login.html",{'msg':"Admin Rejeccted"})
            else:
                request.session["uid"]=user.id
                return redirect("webuser:UserHP")
        elif shopcount>0:
            shop=tbl_shop.objects.get(shop_email=Email,shop_password=Password)
            if shop.shop_vstatus=='0':
                return render(request,"Guest/login.html",{'msg':"Registration Pending"})
            elif shop.shop_vstatus=='2':
                return render(request,'Guest/login.html',{'msg':"Admin Rejected"})
            else:
                request.session["sid"]=shop.id
                return redirect("webshop:ShopHP")
        elif admincount>0:
            admin=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session["aid"] = admin.id
            return redirect("xadmin:AdminHP")
            
        else:
            return render(request,"Guest/login.html",{'msg':'Incorrect Credentials'})
    else:
        return render(request,"Guest/login.html")
    

def Index(request):
    return render(request,'Guest/index.html')


def Contact(request):
    if request.method=="POST":
        tbl_queries.objects.create( queries_name=request.POST.get("txt_name"),
                                    queries_email=request.POST.get("txt_email"),
                                    queries_message=request.POST.get("txt_message"),
                                 )
        return render(request,'Guest/contact.html')
    else:
        return render(request,"Guest/contact.html")

def About(request):
    return render(request,"Guest/about.html")

