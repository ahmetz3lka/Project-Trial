from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Congratulations")
        return redirect("index")
        
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    """if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"register.html",context)
    else:
        form = forms.RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",context)"""
def loginUser(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = LoginForm(request.POST or None)
        context = {
            "form" : form
        }
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,password = password)
            if user is None:
                messages.warning(request,"UserName or password is invalid")
                return render(request,"login.html",context)
            messages.success(request,"Congratulations")
            login(request,user)
            return redirect("index")
        return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.warning(request,"See You...")
    return redirect("index")