from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from .forms import ContactForm,LoginForm

# Create your views here.
def homepage(request):
    context={
        'content':'welcome to the homepage',
      
        
    }
    context['premiun_content']='yeahdjiklkondko'
    return render(request,'homepage.html',context)


def aboutpage(request):
    context={}
    return render(request,'about.html',context)


def contactpage(request):
    contact_form=ContactForm(request.POST or None)
    context={'form':contact_form}
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
   
    return render(request,'contact.html',context)


def login_page(request):
    form=LoginForm(request.POST or None)
    context={'form':form}
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print(form.cleaned_data)
            context['form']=LoginForm()
            return redirect("/login")
        else:
            print("Error")
        
    return render(request,"auth/login.html",context)


def register_page(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data )
    return render(request,"auth/register.html",context)
