# notes/urls.py
from django.urls import path
from . import views1

urlpatterns = [
    path('', views1.notes_list, name='notes'),
    path('signup/', views1.signup_view, name='signup'),
    path('login/', views1.login_view, name='login'),
    path('logout/', views1.logout_view, name='logout'),
    path('note/new/', views1.create_note_view, name='create_note'),
    path('note/<int:pk>/edit/', views1.update_note_view, name='update_note'),
    path('note/<int:pk>/delete/', views1.delete_note_view, name='delete_note'),
    path('note/<int:pk>/', views1.note_detail, name='note_detail')
]
