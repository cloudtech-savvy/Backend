from  django import forms
from django.contrib.auth.models import User
from ceremo_app.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User

# class UserRegisterForm(UserCreationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={'placeholder ':'Username','class':'form-control'}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder ':'Email','class':'form-control'}))
#     password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder ':'Password','class':'form-control'}))
#     password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder ':'Confirm Password','class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password1', 'password2']





class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class VendorRegisterForm(UserRegisterForm):

    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}))
    business_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Business Name', 'class': 'form-control'}))
    business_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Business Type', 'class': 'form-control'}))
    registration_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Registration Number', 'class': 'form-control'}))
    location= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    
    class Meta(UserRegisterForm.Meta):
        fields = UserRegisterForm.Meta.fields + [ 'full_name','business_name', 'business_type', 'registration_number', 'location', 'address']

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder ':'Email','class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder ':'Password','class':'form-control'}) )
    class Meta:
        model = User
        fields = ['email', 'password']

