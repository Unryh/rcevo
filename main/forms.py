# -*- coding: utf-8 -*-
# from django.contrib.auth.models import User
from django import forms
from .models import Advanced_user, Comment_model


class UserForm(forms.ModelForm):
    username = forms.CharField(min_length=3, max_length=40)
    password = forms.CharField(widget=forms.PasswordInput, min_length=5,
                               max_length=40)
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=5,
                                      max_length=40)

    class Meta:
        model = Advanced_user
        fields = ['username', 'password', 'email', 'avatar']

    def clean(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Passwords don't match")

        username = self.cleaned_data.get("username")
        user = Advanced_user.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError("username already taken")



class Comment_form(forms.ModelForm):

    class Meta:
        model = Comment_model
        fields = ['text']


