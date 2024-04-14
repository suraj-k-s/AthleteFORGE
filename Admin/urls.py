from django.urls import path
from django.views import View
from Admin import views
app_name="xadmin"

urlpatterns = [
    path('AdminHP/',views.AdminHP,name="AdminHP"), # type: ignore
    path('ViewProfile/',views.ViewProfile,name="ViewProfile"), #type: ignore
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Logout/',views.Logout,name="Logout"), # type: ignore

    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path("state/",views.state,name="state"),
    path("event/",views.event,name="event"),
    path("district/",views.district,name="district"),
    path("category/",views.category,name="category"),
    path("place/",views.place,name="place"),
    path("scategory/",views.scategory,name="scategory"),

    path("delState/<int:sid>",views.deleteState,name="delState"),
    path("delevent/<int:evid>",views.deleteEvent,name="delevent"),
    path("deldistrict/<int:did>",views.deleteDistrict,name="deldistrict"),
    path("delcategory/<int:cid>",views.deleteCategory,name="delcategory"),
    path("delplace/<int:pid>",views.deletePlace,name="delplace"),
    path("delscategory/<int:scid>",views.deleteScategory,name="delscategory"),

    path("upState/<int:seid>",views.updateState,name="upState"),
    path("upevent/<int:eeid>",views.updateEvent,name="upevent"),
    path("updistrict/<int:eid>",views.updateDistrict,name="updistrict"), 
    path("upcategory/<int:ceid>",views.updateCategory,name="upcategory"),
    path("upplace/<int:peid>",views.updatePlace,name="upplace"),
    path("upscategory/<int:sceid>",views.updateScategory,name="upscategory"), 
    path("CoachVerification/",views.CaochVerification,name="CaochVerification"), 
    path("acceptcoach/<int:aid>",views.acceptcoach,name="acceptcoach"),
    path("RejectCoach/<int:rid>",views.RejectCoach,name="RejectCoach"),
    path("RejectedCoach/",views.RejectedCoach,name="RejectedCoach"),
    path("AcceptedCoach/",views.AcceptedCoach,name="AcceptedCoach"),

    path("ShopVerification/",views.ShopVerification,name="ShopVerification"), 
    path("AcceptShop/<int:aid>",views.AcceptShop,name="AcceptShop"),
    path("RejectShop/<int:rid>",views.RejectShop,name="RejectShop"),
    path("RejectedShop/",views.RejectedShop,name="RejectedShop"),
    path("AcceptedShop/",views.AcceptedShop,name="AcceptedShop"),

    path("UserVerification/",views.UserVerification,name="UserVerification"), 
    path("AcceptUser/<int:aid>",views.AcceptUser,name="AcceptUser"),
    path("RejectUser/<int:rid>",views.RejectUser,name="RejectUser"),
    path("RejectedUser/",views.RejectedUser,name="RejectedUser"),
    path("AcceptedUser/",views.AcceptedUser,name="AcceptedUser"),
    
   ]