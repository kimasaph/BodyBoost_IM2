from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Profile
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=True, label="Age", min_value=1, max_value=120)

    class Meta:
        model = User
        fields = ("username", "age", "password1", "password2")

@login_required
def home(request):
    return render(request, "home.html", {})

def registration_success(request):
    return render(request, "registration_success.html")

def authView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            age = form.cleaned_data.get('age')
            Profile.objects.create(user=user, age=age)
            return redirect("base:registration_success")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})