from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('create/', views.create_note, name='create_note'),
   

    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('search/', views.search_notes, name='search_notes'),
]