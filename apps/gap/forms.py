from django import forms
from django.forms import ImageField, Form, CharField, PasswordInput
from .models import User


class UserRegisterForm(forms.ModelForm):
    avatar = ImageField()
    password = CharField(max_length=128, widget=PasswordInput)

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("avatar", "username", "first_name", "last_name", "email", "is_superuser", "is_staff")


class UserLoginForm(Form):
    username = CharField(max_length=128)
    password = CharField(max_length=128, widget=PasswordInput)
