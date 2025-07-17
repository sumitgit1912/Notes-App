from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def base_redirect(request):
    return redirect('login')

urlpatterns = [
    path('', base_redirect),  # Redirect root URL to login
    path('notes/', include('notesapp.urls')),  # Prefix all app URLs with /notes/
    path('admin/', admin.site.urls),
]
