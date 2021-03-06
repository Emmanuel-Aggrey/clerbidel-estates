from django.urls import path,include
from .import  views

app_name= 'estate_app'
urlpatterns = [
    path('',views.homeview,name='home'),
    path('detailpage/<int:id>/',views.propertydetalview,name='detailpage'),    
    path('contact/',views.Contactview.as_view(),name='contact'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('addland/',views.Addlandview.as_view(),name='addland'),
    path('addhome/',views.Addhomeview.as_view(),name='addhome'),
    path('deleteland/<int:id>/',views.deleteland,name='deleteland'),
    path('deletehome/<int:id>/',views.deletehome,name='deletehome'),
    path('updateland/<int:pk>/',views.Updatelandview.as_view(),name='updateland'),
    path('updatehome/<int:pk>/',views.Updatehomeview.as_view(),name='updatehome'),

]
