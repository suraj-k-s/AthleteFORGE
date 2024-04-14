from django.urls import path,include

from Guest import views
app_name="webguest"
urlpatterns = [
   path('Coach/',views.Coach,name="Coach"),
   path('Shop/',views.Shop,name="Shop"),
   path('User/',views.User,name="User"),
   path('ajaxdistrict/',views.Ajaxdistrict,name="Ajaxdistrict"),
   path('ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
   path('Login/',views.Login,name="Login"),
   path('',views.Index,name="Index"),
   path('Contact/',views.Contact,name="Contact"),
   path('About/',views.About,name="About"),
   
]