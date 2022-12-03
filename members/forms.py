from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields ='__all__'
        exclude=['user']

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields ='__all__'
        widgets={
            'customer': forms.Select(attrs={'class':'form-control','placeholder':'tittle'}),
            'book':forms.Select(attrs={'class':'form-control','placeholder':'Author'}),
            'status':forms.Select(attrs={'class':'form-control','placeholder':'price'}),
            'note':forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
        }

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields ='__all__'
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'tittle'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Author'}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'price'}),
            'category':forms.Select(attrs={'class':'form-control','placeholder':'select catagory'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
        }

class NewMemberForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
            'password1':forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
            'password2':forms.TextInput(attrs={'class':'form-control','placeholder':'confirm password'}),

        }