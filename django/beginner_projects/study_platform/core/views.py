from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm

# Create your views here.

def login_page(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                form.add_error(None,"Invalid username or password.")
    else:
        form=AuthenticationForm()    
    return render(request,"registration/login.html",{'form':form})
    

def register(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("/")
    else:
       form=CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form})
    



