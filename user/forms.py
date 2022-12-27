from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Necles.models import Customer



class CreateNewUser(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']


class CustoumerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'
        exclude=['user']
