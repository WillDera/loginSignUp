from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def signup_view(request):

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
            return redirect('accounts/LoggedIn.html')
    else:
        # create new instance of the UserCreationForm
        form = UserCreationForm()

    # the 3rd param in render is the data being passed down to
    # the template "signup.html"
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # get user details
            user = form.get_user()
            # log the user in
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('djangoblog:article')
    else:
        form = AuthenticationForm
    return render(request, 'accounts/login.html', {'form': form})
