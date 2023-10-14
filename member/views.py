# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from . forms import UserForm
from website.models import CustomUser
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token


# Login user and authentication
def access_granting(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, (f'Hi {username} welcome to your todo list!'))
            return redirect('home')
        else:
            messages.success(request, ('''
            Sorry your username or password does not match!.
            Please enter a valid username or password and try again
            Thank you'''))
            return redirect('granted',)
    else:

        return render(request, 'login.html', {})


def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Getting the variables from the post 
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            # Saving ans instance of user in db with commit == false
            user = form.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            from_email = email
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            receiver = [to_email]
            send_mail(mail_subject, message, from_email,
                      receiver, fail_silently=False)
    return render(request, 'register.html', {})


def user_auth(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
            messages.success(request, f'Welcome {username}')

    return render(request, 'login.html', {})


def signout_user(request):
    logout(request)
    return redirect('/')


def reset_password(request):
    if request.method == "POST":
        user_mail = request.POST.get('email')

        # Send email to user email for verification
        subj = "Verify your email and proceed"
        body = f"New message received {user_mail}"
        print(body)

        user = CustomUser.objects.get(email=user_mail)

    return render(request, 'forget-pass.html')


def activate(request, uidb64, token):
    model = CustomUser
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = model.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
