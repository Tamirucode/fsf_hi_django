from django.contrib import admin
from django.urls import path
from tam import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('findtable', views.findtable, name="findtable"),
    path('bookings', views.bookings, name="bookings"),
    path('deleting', views.deleting, name="deleting"),
    path('mybookings', views.mybookings, name="mybookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),
    path('rebookings', views.rebookings, name="rebookings"),
]
