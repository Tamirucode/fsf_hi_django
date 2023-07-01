from django.contrib import admin
from django.urls import path, include
from tam import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('findtable', views.findtable, name="findtable"),
    path('bookings', views.bookings, name="bookings"),
    path('deleting', views.deleting, name="deleting"),
    path('mybookings', views.mybookings, name="mybookings"),
    
    path('accounts/', include('allauth.urls')),
]
