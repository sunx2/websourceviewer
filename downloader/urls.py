from django.conf.urls import include,url
from . import views
urlpatterns=[
   url(r'^$',views.MainView.as_view(),name="mainview",),
   url(r'^list/$',views.imagelist,name='list',),
   url(r'^help/$',views.helpview,name='help',),
   url(r'^home/$',views.listitems,name="home",),
   
]
