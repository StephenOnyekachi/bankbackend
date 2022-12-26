from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from .models import TrustCall
from .models import Users
from .models import Message
from .models import Loan
from .models import Payment
from .models import Staff
from .models import Contact

# Create your views here.


# for landing pages.
def index(request):

    trustcall = TrustCall.objects.all()

    context = {
        'trustcall': trustcall,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):

    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['text']

        contact = Contact.objects.create(email=email, message=message, name=name)
        messages.success(request, 'message was sent successfully')
        contact.save()

        return redirect('message')
    else:
        Message()

    context = {

    }
    return render(request, 'contact.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('admin_panel')
            else:
                login(request, user)
                return redirect('dashboard')

        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('user_login')
    context = {}

    return render(request, 'login.html')

def user_signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:

            if User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('user_signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                messages.success(request, 'process was successfully, login for the next process')
                # my_dict = {'username': username}
                user.save()

                # html_template = 'email.html'
                # html_message = render_to_string(html_template, context=my_dict)
                # subject = "welcome to standard bank"
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [email]
                # message = EmailMessage(subject, html_message, email_from, recipient_list)
                # message.content_subtype = 'html'
                # message.send()

                return redirect('signup_login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('user_signup')

    context = {

    }

    return render(request, 'signup.html', context)

def signup_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'login success, fill in the form')
            return redirect('signup2')

        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('signup_login')
    context = {}

    return render(request, 'login.html')

@login_required(login_url='user_login')
def signup2(request):

    user = Users.objects.get(name=request.user)

    a = 220
    b = 345
    ab = (str(a) + str(b))
    rand1 = str(random.randint(1000, 9999))
    account_number = ab + rand1
    account_number = int(account_number)

    while len(Users.objects.filter(account_number=account_number)) != 0:
        rand1 = str(random.randint(1000, 9999))
        account_number = ab + rand1
        account_number = int(account_number)

    if request.method == 'POST':
        phone_number = request.POST['phone']
        date_of_birth = request.POST['date']
        gender = request.POST['gender']
        status = request.POST['status']
        address = request.POST['address']

        messages.success(request, 'process completed. account was created successfully, we will send you email')
        user.phone_number = phone_number
        user.date_of_birth = date_of_birth
        user.gender = gender
        user.status = status
        user.address = address
        user.account_number = account_number
        user.save()

        return redirect('dashboard')

    context = {

    }

    return render(request, 'signup2.html', context)

# for dashboards.
@login_required(login_url='user_login')
def admin_panel(request):

    contact = Contact.objects.all().order_by('-id')
    users = Users.objects.all().order_by('-id')
    message = Message.objects.all().order_by('-id')
    loan = Loan.objects.all().order_by('-id')
    payment = Payment.objects.all().order_by('id')

    trustcall = TrustCall.objects.all()

    context = {
        'users': users,
        'message': message,
        'loan': loan,
        'trustcall': trustcall,
        'payment': payment,
        'contact': contact,
    }
    return render(request, 'admin-panel.html', context)

@login_required(login_url='user_login')
def all(request):

    payment = Payment.objects.filter(name=request.user).order_by('id')
    if request.method == 'POST':
        amount = request.POST['amount']
        to = request.POST['to']
        type = request.POST['type']
        message = request.POST['message']

        payment = Payment.objects.create(amount=amount, message=message, to=to, type=type, name=request.user)
        messages.success(request, 'message was sent successfully')
        payment.save()

        return redirect('dashboard')
    else:
        Message()

    context = {
        'payment': payment
    }

    return render(request, 'all.html', context)



# def change(request):
#     return render(request, 'email.html')



@login_required(login_url='user_login')
def dashboard(request):

    user = Users.objects.get(name=request.user)

    # payment = Payment.objects.filter(name=request.user).order_by('-id')
    payment = Payment.objects.all().order_by('-id')

    context = {
        'user': user,
        'payment': payment,
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='user_login')
def loan(request):

    # loan = Loan.objects.all().order_by('-id')
    loan = Loan.objects.filter(name=request.user).order_by('-id')

    if request.method == 'POST':
        amount = request.POST['amount']
        to = request.POST['to']
        message = request.POST['message']

        loan = Loan.objects.create(amount=amount, message=message, to=to, name=request.user)
        messages.success(request, 'message was sent successfully')
        loan.save()

        return redirect('dashboard')
    else:
        Message()

    context = {
        'loan': loan
    }
    return render(request, 'loan.html', context)

@login_required(login_url='user_login')
def message(request):

    inbox_message = Message.objects.filter(name=request.user).order_by('-id')
    # message = Message.objects.all()


    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']

        user_message = Message.objects.create(email=email, message=message, name=request.user)
        messages.success(request, 'message was sent successfully')
        user_message.save()

        return redirect('message')
    else:
        Message()

    context = {
        'inbox_message': inbox_message
    }

    return render(request, 'message.html', context)

@login_required(login_url='user_login')
def profile(request):
    user = Users.objects.get(name=request.user)

    if request.method == 'POST':
        image = request.FILES.get("image")

        user.image = image
        # messages.success(request, 'account was created successfully')
        user.save()
        return redirect('profile')
    else:
       Users()

    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='user_login')
def edit(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        balance = int(request.POST["balance"])

        user.balance = balance
        user.save()
        return redirect('admin_panel')

    context = {
        'user': user
    }
    return render(request, 'edit.html', context)

@login_required(login_url='user_login')
def edit_trustcall(request, pk):
    trustcall = TrustCall.objects.get(id=pk)
    if request.method == 'POST':
        customers = int(request.POST["customers"])
        employees = int(request.POST["employees"])
        deposit = int(request.POST["deposit"])

        trustcall.customers = customers
        trustcall.employees = employees
        trustcall.deposit = deposit
        trustcall.save()
        return redirect('admin_panel')

    context = {
        'trustcall': trustcall
    }
    return render(request, 'edit_trustcall.html', context)

@login_required(login_url='user_login')
def delete(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('admin_panel')
    context = {
        'user': user,
    }
    return render(request, 'delete.html', context)

@login_required(login_url='user_login')
def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('admin_panel')
    context = {
        'message': message,
    }
    return render(request, 'delete_message.html', context)






















