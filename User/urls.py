from django.urls import path,include

from User import views
app_name="webuser"
urlpatterns = [
    path('UserHP/',views.UserHP,name="UserHP"),
    path('ViewUser/',views.ViewUser,name="ViewUser"), # type: ignore
    path('SearchProduct/',views.SearchProduct,name="SearchProduct"),
    path('ProductDetails/<int:id>',views.ProductDetails,name="ProductDetails"),
    path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),
    path('AddCart/<int:id>',views.AddCart,name="AddCart"),
    path('Mycart/',views.Mycart,name="Mycart"),
    path('DelCart/<int:did>',views.DelCart,name="delcart"),
    path('CartQty/',views.CartQty,name="cartqty"),
    path('pay/',views.Pay,name="pay"),
    path('MyBooking/',views.MyBooking,name="MyBooking"),
    path('CancelProduct/<int:id>',views.CancelProduct,name="CancelProduct"),
    path('BookingProducts/<int:id>',views.BookingProducts,name="BookingProducts"),
    path('AjaxCoachSearch/',views.AjaxCoachSearch,name="AjaxCoachSearch"),
    path('SearchCoach/',views.SearchCoach,name="SearchCoach"),
    path('ViewCoach/<int:id>',views.ViewCoach,name="ViewCoach"),
    path('Follow/<int:id>',views.Follow,name="Follow"), 
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxrating/',views.ajaxrating,name="ajaxrating"),

    path('starrating/',views.starrating,name="starrating"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('Contact/',views.Contact,name="Contact"),
    path('About/',views.About,name="About"),
    path('Logout/',views.Logout,name="Logout"),
    path('Trainingdetails/<int:id>',views.Trainingdetails,name="Trainingdetails"),
    path('DailyPlan/<int:id>',views.DailyPlan,name="DailyPlan"),
    path('Workout/<int:id>',views.Workout,name="Workout"),
    path('AjaxCheckbox/',views.AjaxCheckbox,name="AjaxCheckbox"),
    path('subscribe/<int:id>',views.subscribe,name="subscribe"),
    path('subscribepayment/<int:id>/<int:cid>/',views.subscribepayment,name="subscribepayment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),
    path('mysubscription/',views.mysubscription,name="mysubscription"),
    path('subpayment/<int:id>',views.subpayment,name="subpayment"),

    path('checkout/',views.checkout,name="checkout"),




    

    

]
