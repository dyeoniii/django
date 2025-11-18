from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(UserCreationForm):
    email=forms.EmailField(label="이메일")
    phone=forms.CharField(required=False, label="전화번호")
    address=forms.CharField(required=False, label="주소")

    class Meta:
        model=CustomUser
        fields=("username","email", "phone", "address")



