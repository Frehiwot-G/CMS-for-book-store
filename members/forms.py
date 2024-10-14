from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

from django.contrib.auth.forms import SetPasswordForm


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your new password',
            'aria-describedby': 'passwordHelpBlock'
        }),
        help_text="""
            <ul class="list-unstyled">
                <li>Your password can not be too similar to your other personal information.</li>
                <li>Your password must contain at least 8 characters.</li>
                <li>Your password can not be a commonly used password.</li>
                <li>Your password can not be entirely numeric.</li>
            </ul>
        """
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your new password',
        }),
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your new password',
            'aria-describedby': 'passwordHelpBlock'
        }),
        help_text="""
            <ul class="list-unstyled">
                <li>Your password can’t be too similar to your other personal information.</li>
                <li>Your password must contain at least 8 characters.</li>
                <li>Your password can’t be a commonly used password.</li>
                <li>Your password can’t be entirely numeric.</li>
            </ul>
        """
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your new password',
        }),
    )


class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields ='__all__'
        exclude=['user']

class OrderFormCustomer(ModelForm):
    class Meta:
        model=Order
        # fields ='__all__'
        fields = ('customer', 'book', 'note')
        widgets={
            # 'customer': forms.Select(attrs={'class':'form-control','placeholder':'tittle'}),
            'customer':forms.HiddenInput(attrs={'class':'form-control'}),
            'book':forms.Select(attrs={'class':'form-control','placeholder':'Author'}),
            # 'status':forms.Select(attrs={'class':'form-control','placeholder':'price'}),
            'note':forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
        }

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields ='__all__'
        # fields = ('customer', 'book', 'note')
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