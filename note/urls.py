from django.urls import path
from . import views

app_name = 'note'
urlpatterns = [
    # Define your note app URLs here
    # Example: path('notes/', views.note_list, name='note_list'),
    path('',views.note_list.as_view(), name='note-list'),
    path('register/',views.register,name='register'),
    path('note/create/',views.create_note.as_view(), name='note-create'),
    path('note/<int:pk>/edit/',views.edit_note.as_view(), name='note-edit'),
    path('note/<int:pk>/delete/',views.delete_note.as_view(), name='note-delete'),
]