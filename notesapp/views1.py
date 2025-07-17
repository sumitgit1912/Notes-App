from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NoteForm


def signup_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('notes')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Create your views here.
@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes_list.html', {'notes':notes})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_note_view(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit = False)
        note.user = request.user
        note.save()
        return redirect('notes')
    return render(request, 'note_form.html', {'form':form})

@login_required
def update_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('notes')
    return render(request, 'note_form.html', {'form':form})

@login_required
def delete_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'note_form_confirm_delete.html', {'note':note})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'note_detail.html', {'note': note})






