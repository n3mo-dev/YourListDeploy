from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UserRegisterForm
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()   
    return render(request, 'register.html', {'form':form})

@login_required
def todo(request):
    item = Todo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'item':item})

@login_required
def addtodo(request):
    item = request.user.todo_set.create(Data = request.POST['data'])
    return HttpResponseRedirect('/todo/')

@login_required
def deletetodo(request, itemid):
    item  = Todo.objects.get(id=itemid)
    item.delete()
    return HttpResponseRedirect('/todo/') 
