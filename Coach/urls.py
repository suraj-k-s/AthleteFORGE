from django.urls import path
from Coach import views

app_name="webcoach"

urlpatterns = [
 path('CoachHP/',views.CoachHP,name="CoachHP"),
 path('ViewCoach/',views.ViewCoach,name="ViewCoach"), # type: ignore
 path('EditCoach/',views.EditCoach,name="EditCoach"),
 path('EPCoach/',views.EPCoach,name="EPCoach"), # type: ignore
 path('Trainingdetails/',views.Trainingdetails,name="Trainingdetails"),
 path('DailyPlan/<int:id>',views.DailyPlan,name="DailyPlan"),
 path('AddSubscription/',views.AddSubscription,name="AddSubscription"),
 path('Workout/<int:id>',views.Workout,name="Workout"),
 path('Followers/',views.Followers,name="Followers"),

path('chatpage/<int:id>',views.chatpage,name="chatpage"),
path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
path('clearchat/',views.clearchat,name="clearchat"),
]