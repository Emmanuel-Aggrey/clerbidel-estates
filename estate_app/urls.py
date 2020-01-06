from django.urls import path
from .import  views

app_name= 'estate_app'
urlpatterns = [
    path('',views.homeview,name='home'),
    path('detailpage/<slug:slug>/',views.propertydetalview,name='detailpage'),    
    path('contact/',views.Contactview.as_view(),name='contact'),
    path('about/',views.AboutView.as_view(),name='about'),
]
