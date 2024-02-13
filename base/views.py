from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    todo_objects = Todo.objects.all()
    data = {'todos':todo_objects}
    return render(request , 'index.html',context = data) 

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")
        Todo.objects.create(name= name ,description= description , status = status)
        return redirect("home")
    return render(request, 'create.html')

def edit(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")
        
        todo_obj.name = name
        todo_obj.description = description
        todo_obj.status = status
        todo_obj.save()
        return redirect("home")
    return render(request, 'edit.html',{'todo': todo_obj})
    

def delete(request,pk):
    pass