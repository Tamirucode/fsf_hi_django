from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Table, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'tame/home.html')
    else:
        return render(request, 'tame/signin.html')


@login_required(login_url='signin')
def findtable(request):
    context = {}
    if request.method == 'POST':
        number_seats = request.POST.get('number_seats')
        date = request.POST.get('date')
        time = request.POST.get('time')
        table_list = Table.objects.filter(
            number_seats=number_seats, date=date, time=time)
        if table_list:
            return render(request, 'tame/table_list.html', locals())
        else:
            context["error"] = "Sorry table is fullybooked"
            return render(request, 'tame/findtable.html', context)
    else:
        return render(request, 'tame/findtable.html.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_t = request.POST.get('table_id')
        nos = int(request.POST.get('no_seats'))
        table = Table.objects.get(id=id_t)
        if table:
            if table.length < 10:
                table_n = table.table_name
                nos = table.number_seats
                date = table.date
                time = table.time
                name = request.user.username
                email = request.user.email
                userid = request.user.id
                rem_t = table.totallength - table.length
                Table.objects.filter(id=id_t).update(rem=rem_t)
                book = Book.objects.create(username=username, email=email,
                                           userid=userid, table_name=table_n, tableid =id_t,
                                           number_s=nos, date=date, time=time, status='BOOKED')

                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'tame/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'tame/booktable.html', context)

    else:
        return render(request, 'tame/booktable.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_t = request.POST.get('table_id')
        # seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_t)
            table = Table.objects.get(id=book.tableid)
            rem_t = table.rem + book.nos
            Table.objects.filter(id=book.tableid).update(rem=rem_t)
            # nos_r = book.nos - seats_r
            Book.objects.filter(id=id_t).update(status='CANCELLED')
            Book.objects.filter(id=id_t).update(nos=0)
            return redirect(mybookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that table"
            return render(request, 'tame/error.html', context)
    else:
        return render(request, 'tabe/booktable.html')


@login_required(login_url='signin')
def mybookings(request, new={}):
    context = {}
    id_u = request.user.id
    book_list = Book.objects.filter(userid=id_u)
    if book_list:
        return render(request, 'tame/book_list.html', locals())
    else:
        context["error"] = "Sorry no table booked"
        return render(request, 'tame/booktable.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name, email, password, )
        if user:
            login(request, user)
            return render(request, 'tam/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'tame/signup.html', context)
    else:
        return render(request, 'tame/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name
            context["id"] = request.user.id
            return render(request, 'tame/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'tame/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'tame/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'tame/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'tame/success.html', context)
