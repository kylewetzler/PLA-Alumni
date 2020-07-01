from django.shortcuts import render, redirect
from account.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.utils.timezone import now
from global_login_required import login_not_required

@login_not_required
def login_view(request):
    if request.GET:
        next_page = request.GET['next']
    else:
        next_page = "home"
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            print('authenticating')
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_approved:
                    context['inactive'] = 'Your account is still pending approval.'
                else:
                    login(request, user)
                    return redirect(next_page)
        else:
            context['errors'] = form.non_field_errors()

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)

@login_not_required
def logout_view(request):
    context = {}
    user = request.user
    user.last_visit = now()
    user.save()
    context['user'] = user
    logout(request)
    return render(request, 'account/logout.html', context)

@login_not_required
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("valid form")
            form.save()
            email = form.cleaned_data.get('email')
            r_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=r_password)
            #login(request, account)
            return redirect('login')
        else:
            print("invalid")
            print(form.errors)
            context['errors'] = form.errors
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def profile_view(request, user_id):
    context = {}
    user = request.user
    if int(user_id) != user.id:
        return None
    else:
        return render(request, 'account/profile.html', context)
