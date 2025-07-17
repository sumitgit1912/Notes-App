from django.urls import path
from  .views import *

urlpatterns = [
    path('', NotesListView.as_view(), name='notes'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('note/new/', NoteCreateView.as_view(), name='create_note'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='delete_note'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='update_note'),
    path('logout/', CustomLogoutView.as_view(next_page = 'login'), name='logout'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]