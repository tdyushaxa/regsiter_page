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
            return redirect('home')
        return render(request, 'register.html', {"form": form})