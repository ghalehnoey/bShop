from django.shortcuts import redirect, render
from userauths.forms import userRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings

User=settings.AUTH_USER_MODEL
# Create your views here.
def register_view(request):
    if request.method=="POST":
        form=userRegisterForm(request.POST or None)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Hey {username} your account cretaed successfully.")
            new_user=authenticate(username=form.cleaned_data['email'],
                                  password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("core:index")
            
        
    else:
        form=userRegisterForm()
    context={
        'form':form,
    }
    return render(request,"userauths/sign-up.html",context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    if request.method == "POST":
        email= request.POST.get('email')
        password= request.POST.get('password')
        try:
            user=User.objects.all(email=email)
        except:
            messages.warning(request,f"User with {email} Does not exist")

        user=authenticate(request, email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"You are log in")
            return redirect("core:index")
        else:
            messages.warning(request,"User does not exist,Create an account ")
    context={

    }
    return render(request,"userauths/sign-in.html",context)


