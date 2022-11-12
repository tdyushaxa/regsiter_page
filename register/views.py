from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from register.forms import UserCreationForm


# Create your views here.
class HomePageView(View):
    def get(self,request):
        return render(request,'home.html')


class RegisterPageView(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,'register.html',{"form":form})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {"form": form})


class LoginPageView(View):
    def get(self,request):
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})

    def post(self,request):
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')

        return render(request,'login.html',{'form':form})
