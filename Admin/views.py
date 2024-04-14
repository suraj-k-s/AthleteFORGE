from django.shortcuts import render,redirect
import Coach
import User
import Shop
from .models import *
from Guest.models import *


def ViewProfile(request):
    admin = tbl_admin.objects.get(id=request.session["aid"])
    if request.method=="POST":
        return render(request,"Admin/ViewProfile.html"),
    else:
        return render(request,"Admin/ViewProfile.html",{"data":admin})
    






def Logout(request):
    del request.session["aid"]
    return redirect("webguest:Login")
    




def EditProfile(request):
    if 'aid' in request.session:
        admin=tbl_admin.objects.get(id=request.session["aid"])
        if request.method=="POST":
            admin.admin_name=request.POST.get("txt_name")
            admin.admin_contact=request.POST.get("txt_contact")
            admin.save()
            return redirect("xadmin:ViewProfile")
            
        else:
            return render(request,"Admin/EditProfile.html",{"data":admin})
    else:
        return redirect("webguest:Login")
    





def ChangePassword(request):
    if 'aid' in request.session:
        if request.method=="POST":
            admin=tbl_admin.objects.get(id=request.session['aid'])
            opassword=request.POST.get("txt_opassword")
            npassword=request.POST.get("txt_npassword")
            cpassword=request.POST.get("txt_cpassword")
            if admin.admin_password==opassword:
                if npassword == cpassword:
                    admin.admin_password=request.POST.get("txt_npassword")
                    admin.save()
                    return redirect("xadmin:ViewProfile")
                else:
                    msg="password missmatch !"
                    return render(request,"Admin/ChangePassword.html",{'msg':msg})
            else:
                msg="password missmatch !"
                return render(request,"Admin/ChangePassword.html",{'msg':msg})
        else:
            return render(request,"Admin/Changepassword.html")
    else:
        return redirect("webguest:Login")
    





def state(request):
    if 'aid' in request.session:
        state=tbl_state.objects.all()
        if request.method == "POST":
            tbl_state.objects.create(state_name=request.POST.get("txt_state"))
            return render(request,"Admin/state.html",{"state":state})
        else:
            return render(request,"Admin/state.html",{"state":state})
    else:
        return redirect("webguset:Login")




def deleteState(request,sid):
    tbl_state.objects.get(id=sid).delete()
    return redirect("xadmin:state")





def updateState(request,seid):
    data=tbl_state.objects.get(id=seid)
    if request.method=="POST":
        data.state_name=request.POST.get("txt_state")
        data.save()
        return redirect("xadmin:state")
    else:
        return render(request,"Admin/state.html",{"sid":data})
    









def district(request):
    if 'aid' in request.session:
        state=tbl_state.objects.all()
        district=tbl_district.objects.all()
        if request.method == "POST":
            state=tbl_state.objects.get(id=request.POST.get("txt_state"))
            tbl_district.objects.create(district_name=request.POST.get("txt_district"))
            return redirect("xadmin:district")
        else:
            return render(request,"Admin/district.html",{"dist":district,"state":state})
    else:
        return redirect("webgust:Login")




def deleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("xadmin:district")





def updateDistrict(request,eid):
    data=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        data.district_name=request.POST.get("txt_district")
        data.save()
        return redirect("xadmin:district")
    else:
        return render(request,"Admin/district.html",{"dis":data})










def category(request):
    if 'aid' in request.session:
        category=tbl_category.objects.all()
        if request.method=="POST":
            tbl_category.objects.create(category_name=request.POST.get("txt_category"))
            return render(request,"Admin/category.html",{"cat":category,'msg':"Category Inserted"})
        else:
            return render(request,"Admin/category.html",{"cat":category})
    else:
        return redirect("webguest:Login")




def deleteCategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("xadmin:category")





def updateCategory(request,ceid):
    cdata=tbl_category.objects.get(id=ceid)
    if request.method=="POST":
        cdata.category_name=request.POST.get("txt_category")
        cdata.save()
        return redirect("xadmin:category")
    else:
        return render(request,"Admin/category.html",{"cis":cdata})
    









def place(request):
    if 'aid' in request.session:
        district=tbl_district.objects.all()
        place=tbl_place.objects.all()
        if request.method=="POST":
            dist=tbl_district.objects.get(id=request.POST.get("txt_district"))
            tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=dist)
            return redirect("xadmin:place")
        else:
            return render(request,"Admin/place.html",{"plc":place,"dis":district})
    else:
        return redirect("webguest:Login")




def deletePlace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect("xadmin:place")





def updatePlace(request,peid):
    pdata=tbl_place.objects.get(id=peid)
    if request.method=="POST":
        pdata.place_name=request.POST.get("txt_place")
        pdata.save()
        return redirect("xadmin:place")
    else:
        return render(request,"Admin/place.html",{"pis":pdata})
    









def scategory(request):
    if 'aid' in request.session:
        category=tbl_category.objects.all()
        scategory=tbl_scategory.objects.all()
        if request.method=="POST":
            cat=tbl_category.objects.get(id=request.POST.get("txt_category"))
            tbl_scategory.objects.create(scategory_name=request.POST.get("txt_scategory"),category=cat)
            return render(request,"Admin/subcategory.html",{"scat":scategory,"cis":category})
        else:
            return render(request,"Admin/subcategory.html",{"scat":scategory,"cis":category})
    else:
        return redirect("webguest:Login")




def deleteScategory(request,scid):
    tbl_scategory.objects.get(id=scid).delete()
    return redirect("xadmin:scategory")





def updateScategory(request,sceid):
    pdata=tbl_scategory.objects.get(id=sceid)
    if request.method=="POST":
        pdata.scategory_name=request.POST.get("txt_scategory")
        pdata.save()
        return redirect("xadmin:scategory")
    else:
        return render(request,"Admin/subcategory.html",{"scis":pdata})
    








def event(request):
    if 'aid' in request.session:
        event=tbl_event.objects.all()
        if request.method == "POST":
            tbl_event.objects.create(event_name=request.POST.get("txt_event"))
            return render(request,"Admin/event.html",{"event":event})
        else:
            return render(request,"Admin/event.html",{"event":event})
    else:
        return redirect("webguest:Login")




def deleteEvent(request,evid):
    tbl_event.objects.get(id=evid).delete()
    return redirect("xadmin:event")





def updateEvent(request,eeid):
    data=tbl_event.objects.get(id=eeid)
    if request.method=="POST":
        data.event_name=request.POST.get("txt_event")
        data.save()
        return redirect("xadmin:event")
    else:
        return render(request,"Admin/event.html",{"eeid":data})










def CaochVerification(request):
    if 'aid' in request.session:
        coach=tbl_coach.objects.filter(coach_vstatus=0)
        print(coach)
        return render(request,"Admin/coachverification.html",{"vid":coach})
    else:
        return redirect("webguest:Login")




def acceptcoach(request, aid):
    coach=tbl_coach.objects.get(id=aid)
    coach.coach_vstatus="1"
    coach.save()
    return render(request,"Admin/acceptedcoach.html")




def RejectCoach(request, rid):
    coach=tbl_coach.objects.get(id=rid)
    coach.coach_vstatus="2"
    coach.save()
    return render(request,"Admin/rejectedcoach.html")





def RejectedCoach(request):
    if 'aid' in request.session:
        coach=tbl_coach.objects.filter(coach_vstatus=2)
        print(coach)
        return render(request,"Admin/rejectedcoach.html",{"vid":coach})
    else:
        return redirect("webguest:Login")




def AcceptedCoach(request):
    if 'aid' in request.session:
        coach=tbl_coach.objects.filter(coach_vstatus=1)
        print(coach)
        return render(request,"Admin/acceptedcoach.html",{"vid":coach})
    else:
        return redirect("webguest:Login")    









def AdminHP(request):
    if 'aid' in request.session:
        admin = tbl_admin.objects.get(id=request.session["aid"])
        user_pending = tbl_user.objects.filter(user_vstatus=0).count()
        coach_pending = tbl_coach.objects.filter(coach_vstatus=0).count()
        shop_pending = tbl_shop.objects.filter(shop_vstatus=0).count()
        user_accepted = tbl_user.objects.filter(user_vstatus=1).count()
        coach_accepted = tbl_coach.objects.filter(coach_vstatus=1).count()
        shop_accepted = tbl_shop.objects.filter(shop_vstatus=1).count()
        user_rejected = tbl_user.objects.filter(user_vstatus=2).count()
        coach_rejected = tbl_coach.objects.filter(coach_vstatus=2).count()
        shop_rejected = tbl_shop.objects.filter(shop_vstatus=2).count()
        return render(request,'Admin/AdminHP.html',{
            'user_pending': user_pending,
            'coach_pending': coach_pending,
            'shop_-pending': shop_pending,
            'user_accepted': user_accepted,
            'coach_accepted': coach_accepted,
            'shop_accepted': shop_accepted,
            'user_rejected': user_rejected,
            'coach_rejected': coach_rejected,
            'shop_rejected':shop_rejected,
            'data':admin,
        })
    else:
        return redirect("webguest:Login")









def ShopVerification(request):
    if 'aid' in request.session:
        shop=tbl_shop.objects.filter(shop_vstatus=0)
        print(shop)
        return render(request,"Admin/shopverification.html",{"vid":shop})
    else:
        return redirect("webguest:Login")




def AcceptShop(request, aid):
    shop=tbl_shop.objects.get(id=aid)
    shop.shop_vstatus="1"
    shop.save()
    return render(request,"Admin/acceptedshop.html")





def RejectShop(request, rid):
    shop=tbl_shop.objects.get(id=rid)
    shop.shop_vstatus="2"
    shop.save()
    return render(request,"Admin/rejectedshop.html")





def RejectedShop(request):
    if 'aid' in request.session:
        shop=tbl_shop.objects.filter(shop_vstatus=2)
        print(shop)
        return render(request,"Admin/rejectedshop.html",{"vid":shop})
    else:
        return redirect("webguest:Login")




def AcceptedShop(request):
    if 'aid' in request.session:
        shop=tbl_shop.objects.filter(shop_vstatus=1)
        print(shop)
        return render(request,"Admin/acceptedshop.html",{"vid":shop})
    else:
        return redirect("webguest:Login")










def UserVerification(request):
    if 'aid' in request.session:
        user=tbl_user.objects.filter(user_vstatus=0)
        print(user)
        return render(request,"Admin/userverification.html",{"vid":user})
    else:
        return redirect("webguest:Login")




def AcceptUser(request, aid):
    user=tbl_user.objects.get(id=aid)
    user.user_vstatus="1"
    user.save()
    return render(request,"Admin/accepteduser.html")





def RejectUser(request, rid):
    user=tbl_user.objects.get(id=rid)
    user.user_vstatus="2"
    user.save()
    return render(request,"Admin/rejecteduser.html")





def RejectedUser(request):
    if 'aid' in request.session:
        user=tbl_user.objects.filter(user_vstatus=2)
        print(user)
        return render(request,"Admin/rejecteduser.html",{"vid":user})
    else:
        return redirect("webguest:Login")




def AcceptedUser(request):
    if 'aid' in request.session:
        user=tbl_user.objects.filter(user_vstatus=1)
        print(user)
        return render(request,"Admin/accepteduser.html",{"vid":user})
    else:
        return redirect("webguest:Login")

