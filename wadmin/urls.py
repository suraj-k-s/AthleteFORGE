
from django.urls import path
from wadmin import views

urlpatterns = [
    path("add/",views.add),
    path("largest/",views.largest),
    path("mark/",views.mark),
    path("salary/",views.salary),
   ]

