
from itertools import product
from django.shortcuts import render,redirect
from Admin.models import tbl_category, tbl_scategory

from Guest.models import tbl_shop
from Guest.models import tbl_user
from User.models import *

import Shop

from .models import *

# Create your views here.
def ShopHP(request):
    shop = tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        return render(request,"Shop/ShopHP.html")
    else:
        return render(request,"Shop/ShopHP.html",{"data":shop})

def Product(request):
    shop= tbl_shop.objects.get(id=request.session["sid"])
    category=tbl_category.objects.all()
    product=tbl_product.objects.filter(shop=request.session["sid"])
    if request.method == "POST":
        scategory = tbl_scategory.objects.get(id=request.POST.get("txt_scategory"),)
        tbl_product.objects.create(product_name=request.POST.get("txt_name"),
                                 product_price=request.POST.get("txt_price"),
                                 scategory=scategory,
                                 product_discription=request.POST.get("txt_discription"),
                                 product_photo=request.FILES.get("txt_photo"),
                                 shop=shop,                              
                                )   
        return render(request,"Shop/product.html",{"cdata":category,"pdata":product})
    else:
        return render(request,"Shop/product.html",{"cdata":category,"pdata":product})  
    

def MyProducts(request):
    product=tbl_product.objects.filter(shop=request.session["sid"])
    return render(request,"Shop/MyProducts.html",{"pdata":product})
    
def add_photo(request,id):
    pg = tbl_product_gallery.objects.filter(product=id)
    if request.method == "POST":
        pro = tbl_product.objects.get(id=id)
        for files in request.FILES.getlist("txt_photo"):
            tbl_product_gallery.objects.create(product_image=files,product=pro)
        return redirect("webshop:Product")
    else:
        return render(request,"Shop/Add_photo.html",{"pg":pg})
    
def deleteProduct(request,pid):
    tbl_product.objects.get(id=pid).delete()
    return redirect("webshop:Product")

def Ajaxscategory(request):
    sdata=tbl_category.objects.get(id=request.GET.get("categoryid"))
    scdata=tbl_scategory.objects.filter(category=sdata)
    return render(request,"Shop/Ajaxscactegory.html",{"scategory":scdata})


def EPShop(request):
    if request.method=="POST":
        shop=tbl_shop.objects.get(id=request.session['sid'])
        opassword=request.POST.get("txt_opassword")
        npassword=request.POST.get("txt_npassword")
        cpassword=request.POST.get("txt_cpassword")
        if shop.shop_password==opassword:
            if npassword == cpassword:
                shop.shop_password=request.POST.get("txt_npassword")
                shop.save()
                return redirect("webshop:ViewShop")
            else:
                msg="password missmatch !"
                return render(request,"Shop/Changepassword.html",{'msg':msg})
        else:
            msg="password missmatch !"
            return render(request,"Shop/Changepassword.html",{'msg':msg})
    else:
        return render(request,"Shop/Changepassword.html")
    


def ViewShop(request):
    shop = tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        return render(request,"Shop/Viewprofile.html"),
    else:
        return render(request,"Shop/Viewprofile.html",{"data":shop})
    

def EditShop(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        shop.shop_name=request.POST.get("txt_name")
        shop.shop_contact=request.POST.get("txt_contact")
        shop.shop_address=request.POST.get("txt_address")
        shop.save()
        return redirect("webshop:ViewShop")
    else:
        return render(request,"Shop/Editprofile.html",{"data":shop})






def Bookings(request):
    if 'sid' in request.session:
        shop=tbl_shop.objects.get(id=request.session["sid"])
        cartdata=tbl_cart.objects.filter(product__shop=shop)
        shopbookingid = []
        for i in cartdata:
            shopid=i.booking.id
            shopbookingid.append(shopid)
        shopbook=tbl_booking.objects.filter(id__in=shopbookingid,booking_status__gt=1)
        return render(request,"Shop/Viewbooking.html",{'Bookings':shopbook})
    else:
        return render(request,"Shop/Viewbooking.html")



def BookingProducts(request, id):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    booking=tbl_booking.objects.get(id=id)
    cartdata=tbl_cart.objects.filter(booking=booking,product__shop=shop)
    return render(request,"Shop/Viewbookingproduct.html",{"data":cartdata})



def Packed(request,id):
    cartdata=tbl_cart.objects.get(id=id)
    cartdata.cart_status='2'
    cartdata.save()
    return redirect('webshop:Bookings')

    

def Shipped(request,id):
    cartdata=tbl_cart.objects.get(id=id)
    cartdata.cart_status='3'
    cartdata.save()
    return redirect('webshop:Bookings')

def Delivered(request,id):
    cartdata=tbl_cart.objects.get(id=id)
    cartdata.cart_status='4'
    cartdata.save()
    return redirect('webshop:Bookings')




def Contact(request):
    return render(request,'Shop/contact.html')
    

def About(request):
    return render(request,"Shop/about.html")



def Logout(request):
    del request.session["sid"]
    return redirect("webguest:Login")