# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .mixins import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        username = data.get("username")
        password = data.get("password")
        qs = User.objects.filter(username=username)
        print(f'qs == {qs}')
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise forms.ValidationError("Data iz invalid, suka")
        login(request, user)
        self.user = user
        return data

    