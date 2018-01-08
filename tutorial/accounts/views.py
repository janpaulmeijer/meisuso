from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    ProfileForm,
    AddProductForm
)
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Product
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.template import loader
from django.http import HttpResponse



def home(request):
    numbers = [1,2,3,4,5]
    name = 'JP'

    args ={'myname':name, 'numbers':numbers}
    return render(request,'accounts/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

@login_required
def view_profile(request):
    user = request.user
    products = Product.objects.filter(author=request.user)
    template = 'accounts/profile.html'
    return render(request, template, {'products':products,'user': request.user})

#    product=Product.objects.filter(author=request.user)
#    args = {'user':request.user,'product':product}
#    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid:
            form.save() and profile_form.save()
            return redirect('/account/profile')
#        if profile_form.is_valid():
#            profile_form.save()
#            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {'form': form, 'profile_form':profile_form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
    else:
        form = PasswordChangeForm(request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'accounts/add_product.html'
    fields = (
    'product_name',
    'price',
    'category',
    'season',
    'description')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def all_product(request):
    #return HttpResponse("hier komt gewoon wat text")
    products = Product.objects.all()
    template = 'accounts/all_product.html'
    return render(request, template, {'products':products,'user': request.user})
