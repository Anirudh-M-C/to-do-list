from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('update_task/<str:pk>/',views.updatetask,name="_update_task"),
    path('delete_task/<str:pk>/',views.deletetask,name="deletetask")
]
