from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.logged, name="logged"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup")
]
