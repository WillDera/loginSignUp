from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.url')),
    path('admin/', admin.site.urls),
]
