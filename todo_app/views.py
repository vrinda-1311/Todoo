from django.shortcuts import render,redirect

from django.views.generic import View,UpdateView

from todo_app.forms import TaskForm

from todo_app.models import Todo

from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
# Create your views here.

class TakAdd(View):

    def get(self,request):

        form = TaskForm

        return render(request,"add.html",{"form":form})
    
    def post(self,request):

        form = TaskForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            todo = form.save(commit=False)

            todo.user = request.user

            todo.save()

        return redirect("home")        
class ListTask(View):

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        data = Todo.objects.filter(user = request.user)

        return render(request,"list.html",{"data":data})

class DeleteView(View):

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        data = get_object_or_404( Todo,user = request.user,id= id)

        data.delete()

        return redirect('home')
    
class UpdateView(UpdateView):

    model = Todo

    form_class = TaskForm

    template_name = "update.html"

    success_url = reverse_lazy("home")

    def get_queryset(self):

        return Todo.objects.filter(user = self.request.user)
    

class TaskComplete(View):

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        task = get_object_or_404(Todo,user = request.user, id = id)

        task.is_completed = True

        task.save()

        return redirect ("home")