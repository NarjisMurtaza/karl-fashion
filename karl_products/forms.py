from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'image', 'description', 'rating']

class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

# class add_to_cart_form(forms.ModelForm):
#     class Meta:
#         model = cart
#         fields = ['name' , 'name']
