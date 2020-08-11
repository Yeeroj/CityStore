from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product


class UserRegistrationForm(UserCreationForm):
    shopname = forms.CharField()

    mobile = forms.CharField()
    address = forms.CharField()
    time = forms.CharField()
    gstno=forms.CharField()
    holiday = forms.CharField()
    shopowner = forms.CharField()

    class Meta:
        model = User
        fields = [
            'shopname',
            'shopowner','gstno',
            'username', 'password1', 'password2',
            'first_name', 'last_name', 'email',
            'mobile',
            'address', 'time', 'holiday',

        ]


class Productform(forms.ModelForm):

    class Meta:
        model=Product
        fields=[
        'name','image','description','price',
        ]


