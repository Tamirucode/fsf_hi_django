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
        return render(request, 'tam/home.html')
    else:
        return render(request, 'tam/signin.html')


@login_required(login_url='signin')
def findtable(request):
    context = {}
    if request.method == 'POST':
        
        date = request.POST.get('date')
        time = request.POST.get('time')
        table_number = request.POST.get('nost')
        table_list = Table.objects.filter(
             date=date,)
        if table_list:
             return render(request, 'tam/table_list.html', locals())
        else:
           
            context["error"] = "Sorry table is not avilable"
            return render(request, 'tam/findtable.html', context)
    else:
        return render(request, 'tam/findtable.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_table = request.POST.get('table_id')
        number_seats = request.POST.get('nos')
        table_number=request.POST.get('table_number')
        table = Table.objects.get(id=id_table)
        if table:
            if table.reservt > table_number:
                table_name = table.table_name
                nos = table.nos
                date = table.date
                time = table.time
                username = request.user.username 
                email = request.user.email
                user_id = request.user.id
                x = table.reservt - table_number
                Table.objects.filter(id=id_table).update(reservt=x)
                book = Book.objects.create( name=username, email=email, id_table=table_id, user_id=id_user,
                                            table_name=table_name,
                                           nos=nos, date=date, time=time, status='BOOKED')

                
                book.save()
                
                return render(request, 'tam/bookings.html', locals())
            else:
                context["error"] = "Sorry you select unavilable table"
                return render(request, 'tam/findtable.html', context)

    else:
        return render(request, 'tam/findtable.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_table= request.POST.get('table_id')
        # seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_table)
            table = Table.objects.get(id=book.tableid)
            x = table.reservt + book.table_number
            Table.objects.filter(id=book.tableid).update(reservt=x)
            # nos_r = book.nos - seats_r
            Book.objects.filter(id=id_table).update(status='CANCELLED')
            Book.objects.filter(id=id_table).update(table_number=0)
            return redirect(mybookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that table"
            return render(request, 'tam/error.html', context)
    else:
        return render(request, 'tam/findtable.html')


@login_required(login_url='signin')
def mybookings(request, new={}):
    context = {}
    id_table= request.user.id
    book_list = Book.objects.filter(userid = id_table)
    if book_list:
        return render(request, 'tam/book_list.html', locals())
    else:
        context["error"] = "Sorry no table booked"
        return render(request, 'tam/findtable.html', context)


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
            return render(request, 'tam/signup.html', context)
    else:
        return render(request, 'tam/signup.html', context)


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
            return render(request, 'tam/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'tam/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'tam/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'tam/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'tam/success.html', context)
