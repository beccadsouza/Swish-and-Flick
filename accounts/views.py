from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def signup_view( request ):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('spells:list')
        else:
            messages.info(request, "Signup details not entered correctly\nPlease note that, "
                                   "username can be 150 characters or fewer. Letters, digits and @/./+/-/_ only.\n"
                                   "Your password can't be too similar to your other personal information.\n"
                                   "Your password must contain at least 8 characters.\n"
                                   "Your password can't be a commonly used password.\n"
                                   "Your password can't be entirely numeric.")
            return redirect('spells:list')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})


def login_view( request ):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(request.POST.get('next'))
            if 'next' in request.POST:
                return redirect('spells:create')
            else:
                return redirect('spells:list')
        else:
            messages.info(request,
                          'Please enter a correct username and password.\nNote that both fields may be case-sensitive.')
            return redirect('spells:list')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view( request ):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
