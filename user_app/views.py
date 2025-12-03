from django.shortcuts import render,redirect

from django.views.generic import View

from user_app.forms import UserregistarionForm

from user_app.models import User

from django.contrib.auth import authenticate,login,logout

from todo_app.models import Todo

# Create your views here.


class RegistrationView(View):

    def get(self,request):

        form = UserregistarionForm()

        return render(request,"signup.html",{"form":form})
    
    def post(self,request):

        username = request.POST.get("username")

        first_name = request.POST.get("first_name")

        last_name = request.POST.get("last_name")

        password = request.POST.get("password")

        email = request.POST.get("email")

        User.objects.create_user( username = username,
                            first_name = first_name,
                            last_name = last_name,
                            password = password,
                            email = email)
        
        form = UserregistarionForm
        
        return redirect("login")
    
class LoginView(View):

    def get(self,request):

        return render (request,"signin.html")
    
    def post(self,request):

        username = request.POST.get("username")

        password = request.POST.get("password")

        User = authenticate(request, username = username,password = password)

        if User:

            login(request,User)

            return redirect("home")
        
        return render(request,"signin.html")

class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect ("login")
    
class BaseView(View):

    def get(self,request):
        
        todo = Todo.objects.filter(user = request.user)

        return render(request,"home.html",{"todo":todo})





