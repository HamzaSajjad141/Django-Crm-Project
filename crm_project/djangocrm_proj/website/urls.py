from django.urls import path
from . import views
urlpatterns = [
    path('', views.func,name='Home'),
    #path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
   





   
    path('hamza/', views.ham),
    path('main/', views.home1),
    path('works/', views.h1),
    path('f/', views.func2),
    path('dishes/<str:dish>',views.menuitems), 


]
