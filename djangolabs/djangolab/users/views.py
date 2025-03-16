# from django.shortcuts import render
from django.views import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .form import SigninForm, SignupForm
from django.contrib.auth.models import User
# from django.contrib.auth import logout
# from django.shortcuts import redirect
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth.forms import UserCreationForm
# from .form import SigninForm
# # Create your views here.
# class LogoutView(View):
#     def get(self,request):
#         logout(request)
#         return redirect('Login')

# class LoginView(View):
#      def get(self,req):
#         context={'form':SigninForm()}
#         return render(req,'users/login.html',context)
#      def post(self,req):
#         logeduserobj=Usernative.objects.filter(
#             username=req.POST['username'],
#             password=req.POST['password']).first()
#         loggedauthuserobj=authenticate(
#                 username=req.POST['username'],
#                 password=req.POST['password'])
#         if(logeduserobj is not None and loggedauthuserobj):
#             ##sesion
#             req.session['id']=logeduserobj.id
#             req.session['name']=logeduserobj.username
#             login(req)
#             return redirect('listt')
#         else:
#             return render(request,'users/login.html',{'form':form})



# class Signup(View):
#     def get(self,req):
#         context={'form':SignupForm()}
#         return render(req,'nativr/reg.html',context)
#     def post(self,req):
#         form=SignupForm(data=req.POST)
#         if(form.is_bound and form.is_valid()):
#             form.save()
#             User.objects.create_user(username=form.clean_data['username'],
#                                      password=form.clean_data['password'],
#                                      isactive=True)
#             return redirect('Loginnative')
#         else:
#             context={
#                 'form':form,
#                 'msg':form.errors
#             }
#             return render(req, 'nativr/reg.html', context)
class LoginView(View):
    def get(self, request):
        context = {'form': SigninForm()}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/trainee')
        return render(request, 'users/login.html', {'form': form})

class SignupView(View):
    def get(self, request):
        context = {'form': SignupForm()}
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('listt')
        return render(request, 'users/register.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')