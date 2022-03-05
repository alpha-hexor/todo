from django.urls import path
from home import views


urlpatterns = [
    path("",views.home,name="home"),
    path("tasks",views.task,name="tasks"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('update/<str:item_id>', views.update, name="update"),
]