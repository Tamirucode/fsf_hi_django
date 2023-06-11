from django.contrib import admin
from django.urls import path
from tam import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('findtable', views.findtable, name="findtable"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('mybookings', views.mybookings, name="mybookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),

]
