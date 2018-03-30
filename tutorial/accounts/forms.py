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
                'placeholder': 'What is your hometown?'
            }
        )
    )
    country = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }
        )
    )
    customer_role = (
        ('Buyer', 'Buyer'),
        ('Producer', 'Producer'),
        ('Other', 'Other'),
    )

    role = forms.CharField(label='Role',
    widget=forms.Select(choices=customer_role))



    address1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Address line 1'
            }
        )
    )

    address2 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Address line 2'
            }
        )
    )

    website = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Website'
            }
        )
    )

    postcode = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Postcode'
            }
        )
    )

    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'State'
            }
        )
    )


    phone = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }
        )
    )

    company = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Company name'
            }
        )
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your first name here'
            }
        )
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your last name here'
            }
        )
    )

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Pick a cool username'
            }
        )
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'What is your e-mail address?'
            }
        )
    )

    password1 = forms.CharField(
        max_length = 100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Pick a secure password'
            }
        )
    )

    password2 = forms.CharField(
        max_length = 100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat your password'
            }
        )
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
        'country',
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
country = forms.CharField(
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
