from tabnanny import check
from django.shortcuts import render,redirect


from django.db.models import Q
from Guest.models import *
from Shop.models import tbl_product
from Admin.models import *
from Shop.views import *
from User.models import tbl_booking
from django.http import JsonResponse
from .models import *
from Coach.models import *
from datetime import datetime

# Create your views here.
def UserHP(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        return render(request,"User/UserHP.html")
    else:
        return render(request,"User/UserHP.html",{"data":user})
    


def ViewUser(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        return render(request,"User/viewprofile.html"),
    else:
        return render(request,"User/viewprofile.html",{"data": user})
    
def SearchProduct(request):
    product=tbl_product.objects.all()
    return render(request,"User/searchproduct.html",{"data":product})

def ProductDetails(request,id):
    product=tbl_product.objects.get(id=id)
    return render(request,"User/Productdetails.html",{"data":product})


def ajaxsearch(request):
    products = tbl_product.objects.filter(product_name__istartswith=request.GET.get("pname"))
    return render(request,"User/AjaxSearch.html",{"products":products})



def AddCart(request,id):
    product=tbl_product.objects.get(id=id)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=product).count()
        if cartcount>0:
            msg='Already Added'
            return render(request,"User/Productdetails.html",{"data":product,"msg":msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=product)
            msg='Added to Cart'
            return render(request,"User/Productdetails.html",{"data":product,"msg":msg})
    else:
        tbl_booking.objects.create(user=userdata)
        bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=product).count()
            if cartcount>0:
                msg='Already Added'
                return render(request,"User/Productdetails.html",{"data":product,"msg":msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=product)
                msg='Added to Cart'
                return render(request,"User/Productdetails.html",{"data":product,"msg":msg})
        else:
            msg='Somthing Wrong'
            return render(request,"User/Productdetails.html",{"data":product,"msg":msg})
        


def Mycart(request):
   if request.method=="POST":
     bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
     bookingdata.booking_amount=request.POST.get("carttotalamt")
     bookingdata.booking_status='1'
     bookingdata.save()
     cartdata=tbl_cart.objects.filter(booking=bookingdata)
     for i in cartdata:
         i.cart_status='1'
         i.save()
     return redirect("webuser:pay")
   else:
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
   #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
    if bcount>0:
    #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
     book=tbl_booking.objects.get(user=customerdata,booking_status=0)
     bid=book.id
     request.session["bookingid"]=bid
     bkid=tbl_booking.objects.get(id=bid)
     cartdata=tbl_cart.objects.filter(booking=bkid)
     return render(request,"User/MyCart.html",{'data':cartdata})
    else:
      return render(request,"User/MyCart.html")
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("webuser:Mycart")
def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_quantity=qty
   cartdata.save()
   return redirect("webuser:Mycart")

def Pay(request):
   if request.method=="POST":
        bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_status='2'
        bookingdata.save()
        return redirect("webuser:UserHP")
   else:
        return render(request,"User/Payment.html")
   
def MyBooking(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingdata=tbl_booking.objects.filter(user=request.session["uid"],booking_status__gt=1)
    return render(request,"User/Viewbooking.html",{'data':bookingdata})

def CancelProduct(request, id):
    cart=tbl_cart.objects.get(id=id)
    cart.cart_status='5'
    cart.save()
    bookingData=tbl_booking.objects.get(id=cart.booking_id)
    cartCount=tbl_cart.objects.filter(booking=bookingData, cart_status__lt=5).count()
    print(cartCount)
    if(cartCount==0):
        bookingData.booking_status='3'
        bookingData.save()
    return redirect("webuser:MyBooking")
    

def BookingProducts(request, id):
    booking=tbl_booking.objects.get(id=id)
    cartdata=tbl_cart.objects.filter(booking=booking)
    return render(request,"User/Viewbookingproduct.html",{"data":cartdata})
    
    
def SearchCoach(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    coach=tbl_coach.objects.all()
    for i in coach:
        wdata=tbl_coach.objects.get(id=i.id)
        tot=0
        ratecount=tbl_rating.objects.filter(coach=wdata).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(coach=wdata)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)  
    datas=zip(coach,parry)
    return render(request,"User/searchcoach.html",{"data":datas,"ar":ar})


def AjaxCoachSearch(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    coach = tbl_coach.objects.filter(event__event_name__istartswith=request.GET.get("cname"))
    for i in coach:
        wdata=tbl_coach.objects.get(id=i.id)
        tot=0
        ratecount=tbl_rating.objects.filter(coach=wdata).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(coach=wdata)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)  
    datas=zip(coach,parry)
    return render(request,"User/AjaxCoachSearch.html",{"coach":datas,"ar":ar})





def ViewCoach(request,id):
    coach = tbl_coach.objects.get(id=id)
    subcount =  tbl_subscribe.objects.filter(user=request.session["uid"],status=1).count()
    print(subcount)
    value = 0
    if subcount > 0:
        value = 1
    return render(request,"User/ViewCoach.html",{'data':coach,"value":value})
    


def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    wdata=tbl_coach.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(coach=wdata).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(coach=wdata).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'cid':mid})

def ajaxrating(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_coach.objects.get(id=workid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,coach=wdata)
    stardata=tbl_rating.objects.filter(coach=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    car_id = request.GET.get("pdt")
    cdata = tbl_coach.objects.get(id=car_id)
    rate = tbl_rating.objects.filter(coach=cdata)

    for i in rate:
        if int(i.rating_data) == 5:
            five += 1
        elif int(i.rating_data) == 4:
            four += 1
        elif int(i.rating_data) == 3:
            three += 1
        elif int(i.rating_data) == 2:
            two += 1
        elif int(i.rating_data) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)




def Follow(request,id):
    tbl_follow.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),coach=tbl_coach.objects.get(id=id))
    return redirect("webuser:SearchCoach")

def chatpage(request,id):
    user  = tbl_coach.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_user = tbl_coach.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,coach_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(coach_from=tid) | Q(coach_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(coach_to=request.GET.get("tid")) | (Q(coach_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})




def Contact(request):
    if request.method == "POST":
        tbl_queries.objects.create(queries_name=request.POST.get("txt_name"),queries_email=request.POST.get("txt_email"),queries_message=request.POST.get("txt_message"))
        return redirect("webuser:Contact")
    else:
        return render(request,'User/contact.html')
    

def About(request):
    return render(request,"User/about.html")



def Logout(request):
    del request.session["uid"]
    return redirect("webguest:Login")



def Trainingdetails(request,id):
    event=tbl_event.objects.get(id=id)
    training=tbl_trainig.objects.filter(event_id=event)
       
    return render(request,"User/ViewTraining.html",{"data":event,"tdata":training})

def subscribe(request,id):
    pack = tbl_subscription.objects.filter(coach=id)
    return render(request,"User/View_Package.html",{"pack":pack,"cid":id})

def subpayment(request,id):
    pack = tbl_subscribe.objects.get(id=id)
    amt = pack.subscription.subscription_amount
    # print(amt)
    if request.method == "POST":
        subs = tbl_subscribe.objects.get(id=id)
        subs.status = 1
        subs.save()
        return redirect("webuser:loader")
    else:
        return render(request,"User/Payment.html",{"total":amt})

def subscribepayment(request,id,cid):
    pack = tbl_subscription.objects.get(id=id)
    amt = pack.subscription_amount
    if request.method == "POST":
        subs = tbl_subscribe.objects.get(id=request.session["subid"])
        subs.status = 1
        subs.save()
        return redirect("webuser:loader")
    else:
        subcount = sub = tbl_subscribe.objects.filter(user=request.session["uid"],status=0).count()
        if subcount > 0:
            return render(request,"User/View_Package.html",{"msg":"already subscribed...","cid":cid})
        else:
            tbl_subscribe.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),subscription=tbl_subscription.objects.get(id=id))
            sub = tbl_subscribe.objects.get(user=request.session["uid"],status=0)
            request.session["subid"] = sub.id
            return render(request,"User/Payment.html",{"total":amt})
    
def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def mysubscription(request):
    data = tbl_subscribe.objects.filter(user=request.session["uid"])
    return render(request,"User/My_subscription.html",{"data":data})


def DailyPlan(request,id):
    dailyplan=tbl_dailyplan.objects.all()
    training = tbl_trainig.objects.get(id=id)
    return render(request,"User/DailyPlan.html",{"data":dailyplan})


# def Workout(request, id):
#     workouts = tbl_workout.objects.filter(dailyplan=id)
#     user_id = request.session.get("uid", None)
    
#     if user_id:
#         checkbox_exists = [tbl_checkbox.objects.filter(user=user_id, workout=workout).exists() for workout in workouts]
#     else:
#         checkbox_exists = [False] * len(workouts)

#     data = list(zip(workouts, checkbox_exists))

#     return render(request, "User/Workout.html", {"data": data})


def Workout(request, id):
    workouts = tbl_workout.objects.filter(dailyplan=id)
    user_id = request.session.get("uid", None)
    total_workouts = workouts.count()
    checked_workouts = tbl_checkbox.objects.filter(user=user_id, workout__in=workouts).count()
    progress_percentage = (checked_workouts / total_workouts) * 100 if total_workouts > 0 else 0

    if user_id:
        checkbox_exists = [tbl_checkbox.objects.filter(user=user_id, workout=workout).exists() for workout in workouts]
    else:
        checkbox_exists = [False] * len(workouts)

    data = list(zip(workouts, checkbox_exists))

    return render(request, "User/Workout.html", {"data": data, "progress_percentage": progress_percentage})





def AjaxCheckbox(request):
    workout=tbl_workout.objects.get(id=request.GET.get("wid"))
    check=tbl_checkbox.objects.filter(user=request.session["uid"],workout=workout).count()
    if check>0: 
        tbl_checkbox.objects.get(user=request.session["uid"],workout=workout).delete()
        return redirect("webuser:AjaxCheckbox")
    else:
        tbl_checkbox.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),workout=workout)
        return JsonResponse({"msg":"Updated"})



def checkout(request):
    return render(request,"User/checkout.html")