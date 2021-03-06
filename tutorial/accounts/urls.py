from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.home, name='home'),
    path('login', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.view_profile, name='view_profile'),
    path('my-product', views.my_product, name='my-product'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change-password', views.change_password, name='change_password'),
#    path('add-product', views.add_product, name='add_product'),
    path('add-product/', views.ProductCreateView.as_view(), name='add_product'),
    path('all-product/', views.all_product, name='all-product'),
    path('all-users', views.all_users, name='all-users'),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('signupnewsletter', views.signupnewsletter, name='signupnewsletter'),



]
