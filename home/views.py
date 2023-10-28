from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm 
  
from django.contrib.auth.decorators import login_required ,user_passes_test 
  
from django.contrib import messages 
  
from .forms import CreateUserForm
from .models import * 
  
from django.core.mail import send_mail 
from django.conf import settings 
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage,EmailMultiAlternatives 
  
from django.views.decorators.cache import never_cache 
 

def register(request): 
   if request.user.is_authenticated: 
     return redirect('home') 
   else: 
     form = CreateUserForm() 
     if request.method == 'POST': 
       form = CreateUserForm(request.POST) 
       if form.is_valid(): 
         form.save() 
         user = form.cleaned_data.get('username') 
  
         subject = f'AUCTIONG REGISTRATION' 
         message = 'Account Register Confirmation ' 
         recepiant = form.cleaned_data.get('email') 
         user = form.cleaned_data.get  ('username') 
         context ={ 
           'user' : user 
         } 
         card_html = render_to_string('registeremail.html', context) 
  
         email = EmailMultiAlternatives(subject, message,settings.EMAIL_HOST_USER, [recepiant]) 
  
         email.attach_alternative(card_html, 'text/html') 
         email.send(fail_silently=False) 
  
         messages.success(request,'success') 
  
         messages.success(request,'Account created for '+ user) 
         return redirect('login') 
  
   context ={ 'form' :form} 
   return render(request,'register.html', context) 
  
 
def user_login(request): 
   if request.user.is_authenticated: 
     return redirect('home') 
   else: 
     if request.method == 'POST': 
  
       username = request.POST.get('username') 
       password = request.POST.get('password') 
       user = authenticate(request, username = username, password = password) 
       if user is not None: 
         login(request,user) 
         return redirect('home') 
       else: 
         messages.success(request,'Invalid Credential') 
         return render(request,'login.html') 
  
   context = {} 
   return render(request,'login.html', context) 
  
  
  
  
  
def logout_user(request): 
  logout(request) 
  return redirect('login') 
  
  
  
@login_required(login_url ='login')  
def index(request): 
  return render(request, 'home.html') 
  
  
@login_required(login_url ='login')    
def about(request): 
  return render(request, 'about.html') 
 
 
@login_required(login_url ='login')  
def contact(request): 
  return render(request, 'contact.html') 
  
def is_admin(user): 
     return user.is_staff  # Assuming staff members are admins 