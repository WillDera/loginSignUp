from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path("LoggedIn/", views.logged, name="loggedIn"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup")
]
