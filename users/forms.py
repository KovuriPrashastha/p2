from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#class
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #this class meta keeps all the names in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    mail = forms.EmailField()

    class Meta:
        #this class meta keeps all the names in one place
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



