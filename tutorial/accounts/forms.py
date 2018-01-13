from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Product
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your name here'
            }
        )
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your name here'
            }
        )
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your name here'
            }
        )
    )

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your name here'
            }
        )
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
        'class': 'form-control'})
    )

    password1 = forms.CharField(
        max_length = 100,
        widget=forms.PasswordInput(attrs={
        'class': 'form-control'})
    )

    password2 = forms.CharField(
        max_length = 100,
        widget=forms.PasswordInput(attrs={
        'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
        'first_name',
        'last_name',
        'email',
        'password'
        )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your name here'
            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your name here'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
        'class': 'form-control'})
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description',
        'city',
        'website',
        'phone')
description = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your name here'
        }
    )
)
city = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your name here'
        }
    )
)
website = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your name here'
        }
    )
)
phone = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your name here'
        }
    )
)

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
        'product_name',
        'price',
        'category',
        'season',
        'description'
        )
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'season': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }
