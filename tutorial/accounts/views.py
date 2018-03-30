from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    ProfileForm,
    AddProductForm
)
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Product, User, BlogItem
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.template import loader
from django.http import HttpResponse, Http404
from geopy.geocoders import Nominatim


def home(request):
    blogitems = BlogItem.objects.all()
    template = 'accounts/home.html'
    return render(request, template, {'blogitems':blogitems,'user': request.user})

def signupnewsletter(request):
    numbers = [1,2,3,4,5]
    name = 'JP'

    args ={'myname':name, 'numbers':numbers}
    return render(request,'accounts/signupnewsletter.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.userprofile.city = form.cleaned_data.get('city')
            user.userprofile.country = form.cleaned_data.get('country')
            user.userprofile.address1 = form.cleaned_data.get('address1')
            user.userprofile.address2 = form.cleaned_data.get('address2')
            user.userprofile.state = form.cleaned_data.get('state')
            user.userprofile.postcode = form.cleaned_data.get('postcode')
            user.userprofile.company = form.cleaned_data.get('company')
            user.userprofile.role = form.cleaned_data.get('role')
            geolocator = Nominatim()
            fulladdress = user.userprofile.city+' '+user.userprofile.country+' '+user.userprofile.postcode+' '+user.userprofile.address1
            location = geolocator.geocode(fulladdress)
            user.userprofile.lat = location.latitude
            user.userprofile.lon = location.longitude
            print(user.userprofile.city+' '+user.userprofile.country+' '+user.userprofile.postcode+' '+user.userprofile.address1)
            print(location.latitude, location.longitude)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('/account/my-product')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/reg_form.html', {'form': form})

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

@login_required
def my_product(request):
    user = request.user
    products = Product.objects.filter(author=request.user)
    template = 'accounts/my_product.html'
    return render(request, template, {'products':products,'user': request.user})

class ProductDetailView(DetailView):
    model = Product

@login_required
def all_users(request):
    users = User.objects.all()
    profiles = UserProfile.objects.filter(role='Producer')
    template = 'accounts/all_users.html'
    return render(request, template, {'profiles':profiles})

#class AllUserView(ListView):
#    context_object_name = 'all-users'
#    template_name = 'accounts/all_users.html'
#    queryset = User.objects.get()
#    model = User

#    def get_context_data(self, **kwargs):
#         context = super(AllUserView, self).get_context_data(**kwargs)
#         context['profile'] = UserProfile.objects.get()
#         context['user'] = self.queryset

#         return context
