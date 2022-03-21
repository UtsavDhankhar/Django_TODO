from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.


def taskList(request):

    model = Task.objects.all()
    return render(request , 'base/tasklist.html' , {'model': model})


def detail_view(request , pk):

    model = Task.objects.get(pk=pk)
    return render(request , 'base/task_detail.html' , {'detail': model})



def create_task(request):

    if(request.method=='POST'):
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()

        return redirect('task_list')

    task = TaskForm()
    return render(request , 'base/create_task.html' , {'task':task})


def update_task(request, pk):

    object = get_object_or_404(Task , pk=pk)

    if(request.method=='GET'):
        task = TaskForm(instance=object)
        return render(request , 'base/update-task.html' , {'task': task})


    task = TaskForm(request.POST , instance=object)
    if(task.is_valid()):
        task.save()
    
    return redirect('task_list')


def delete_task(request,pk):
    object = get_object_or_404(Task , pk=pk)

    if(request.method=="POST"):
        object.delete()
        return redirect('task_list')

    return render(request , 'base/delete.html' , {'task':object})
    
