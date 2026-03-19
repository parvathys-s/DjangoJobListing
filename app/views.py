from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from app.forms import SignUpForm,LoginForm,AddJob
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from app.models import Job


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,'home.html')

class Register(View):
    def get(self, request):
        form_instance = SignUpForm()
        context = {'form':form_instance}
        return render(request,'register.html',context)

    def post(self, request):
        form_instance = SignUpForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
        return redirect("app:home")


class AdminHome(View):
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, 'adminhome.html', {'jobs': jobs})


class UserHome(View):
    def get(self, request):
        jobs = Job.objects.filter(isActive=True)
        return render(request, 'userhome.html', {'jobs': jobs})

class Login(View):
    def get(self, request):
        form_instance = LoginForm()
        context = {'form':form_instance}
        return render(request,'login.html',context)
    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            u=data['username']
            p=data['password']
            #authenticate()
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_superuser==True:
                    login(request, user)
                    return redirect("app:adminhome")

                else:
                    login(request, user)
                    return redirect("app:userhome")
            else:
                messages.error(request,"Invalid username or password.")
                return redirect("app:login")

        return render(request, "login.html", {'form': form_instance})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('app:login')

class Delete(View):
    def get(self, request,i):
        m = Job.objects.get(id=i)
        m.delete()
        return redirect('app:adminhome')


class Add(View):
    def get(self, request):
        form = AddJob()
        return render(request, "job_form.html", {'form': form})

    def post(self, request):
        form = AddJob(request.POST)

        if form.is_valid():
            form.save()
            return redirect('app:adminhome')

        return render(request, "job_form.html", {'form': form})

class Update(View):
    def get(self, request, i):
        job = Job.objects.get(id=i)
        form = AddJob(instance=job)   # 👈 pre-fill data
        return render(request, "job_form.html", {'form': form})

    def post(self, request, i):
        job = Job.objects.get(id=i)
        form = AddJob(request.POST, instance=job)  # 👈 update same object

        if form.is_valid():
            form.save()
            return redirect('app:adminhome')

        return render(request, "job_form.html", {'form': form})