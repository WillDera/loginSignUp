from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):

    # check if request is a POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # verify if the inputs are valid and also,
        # check if user already exists
        if form.is_valid():
            # retrieve user sign up details then
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('accounts:loggedIn')
    else:
        # create new instance of the UserCreationForm
        form = UserCreationForm()

    # the 3rd param in render is the data being passed down to
    # the template "signup.html"
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:loggedIn')
    else:
        form = AuthenticationForm
    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='accounts:login')
def logged(request):
    return render(request, 'accounts/loggedIn.html')
