from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']   
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5 , 'placeholder': 'Enter note content'}),
        }

class RegistrationFrom(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {field_name.replace("_", " ").title()}'
            })