from django.urls import path,include

from Shop import views
app_name="webshop"
urlpatterns = [
     path('ShopHP/',views.ShopHP,name="ShopHP"),
     path('Ajaxscategory/',views.Ajaxscategory,name="Ajaxscategory"),
     path('Product/',views.Product,name="Product"),
     path('deleteProduct<int:pid>',views.deleteProduct,name="deleteProduct"),
     path('add_photo/<int:id>',views.add_photo,name="add_photo"),
     path('ViewShop/',views.ViewShop,name="ViewShop"),# type: ignore
     path('EPShop/',views.EPShop,name="EPShop"),
     path('EditShop/',views.EditShop,name="EditShop"),
     path('Booking/',views.Bookings,name="Bookings"),# type: ignore
     path('BookingProducts/<int:id>',views.BookingProducts,name="BookingProducts"),
     path('Packed/<int:id>',views.Packed,name="Packed"),
     path('Shipped/<int:id>',views.Shipped,name="Shipped"),
     path('Delivered/<int:id>',views.Delivered,name="Delivered"),
     path('Contact/',views.Contact,name="Contact"),
     path('About/',views.About,name="About"),
     path('Logout/',views.Logout,name="Logout"),
     path('MyProducts/',views.MyProducts,name="MyProducts"),

  
]