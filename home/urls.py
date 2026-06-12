
from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path("createuser", views.createuser, name='createuser'),
    # path('create-note/', views.create_note, name='create_note'),
    # path('notes/', views.notes, name='notes'),
    # # path('read-notes/', views.read_notes, name='read_notes'),
    # # path('view-notes/', views.view_notes, name='view_notes'),
    # path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
    # path('search/', views.search_notes, name='search_notes'),
    # path("login/", views.loginuser, name='loginuser'),
    # path("logout/", views.logoutuser, name='logoutuser'),
    # path("submitcreateuser", views.createuser, name='createuser'),
]
