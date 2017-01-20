# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from .models import Advanced_user, Comment_model, Test_db


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Advanced_user
        fields = ['username', 'password', 'avatar']


class Comment_form(forms.ModelForm):

    class Meta:
        model = Comment_model
        fields = ['text']

class Test_Comment_form(forms.ModelForm):

    class Meta:
        # model = Advanced_user
        # fields = ['avatar']
        model = Test_db
        fields = ['comment_text']