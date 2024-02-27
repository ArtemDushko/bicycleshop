from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    authority = forms.ChoiceField(choices=Profile.AUTHORITY_TYPE)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "authority")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.filter(user=user).update(authority=self.cleaned_data.get('authority'))
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)