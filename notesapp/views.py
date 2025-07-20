from gettext import npgettext
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.db.models import Q


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'notes'
    paginate_by = 5  # Show 5 notes per page

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Note.objects.filter(user=self.request.user)
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset.order_by('-timestamp')

    
class SignupView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('notes')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('notes')
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note_form.html'
    success_url = reverse_lazy('notes')
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "✅ Note created successfully!")
        return super().form_valid(form)
    
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'note_form.html'
    model = Note
    success_url = reverse_lazy('notes')
    fields = ['title', 'content']
    def get_queryset(self):
        messages.info(self.request, "📝 Note updated successfully.")
        return Note.objects.filter(user=self.request.user)
    
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'note_form_confirm_delete.html'
    model = Note
    success_url = reverse_lazy('notes')
    def get_queryset(self):
        messages.warning(self.request, "🗑️ Note deleted.")
        return Note.objects.filter(user=self.request.user)
    
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'note_detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
class CustomLogoutView(LoginRequiredMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "👋 You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
    
# To create superuser by script not command 
# Run once during startup (not safe for production)
# from django.contrib.auth import get_user_model
# User = get_user_model()

# if not User.objects.filter(username="admin").exists():
#     User.objects.create_superuser("admin", "admin@example.com", "securepassword")

