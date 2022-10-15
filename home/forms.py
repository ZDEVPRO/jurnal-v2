from django.forms import ModelForm, TextInput, Textarea, EmailInput
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'first_name': TextInput(attrs={'type': 'text', 'placeholder': 'Ism *'}),
            'last_name': TextInput(attrs={'type': 'text', 'placeholder': 'Familya *'}),
            'email': TextInput(attrs={'type': 'email', 'placeholder': 'Email *'}),
            'phone': TextInput(attrs={'type': 'number', 'placeholder': 'Telefon raqam *'}),
            'message': Textarea(attrs={'type': 'text', 'placeholder': 'Sizning xabaringiz *'})
        }


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
