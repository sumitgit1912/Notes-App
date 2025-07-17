from django import forms
from . models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',  # Single space for floating label
                'id': 'id_title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ' ',  # Single space for floating label
                'style': 'height: 150px;',
                'id': 'id_content',
            }),
        }
