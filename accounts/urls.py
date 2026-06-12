from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.createuser, name='createuser'),
    path("login/", views.loginuser, name='loginuser'),
    path("logout/", views.logoutuser, name='logoutuser'),
    path("check-username/",views.check_username,name="check_username"),
    path("check-email/",views.check_email,name="check_email"),
]