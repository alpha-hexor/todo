from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Task
# Create your views here.

def home(request):
    context={'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        
        #save the data to the database
        d=Task(TaskTitle=title,TaskDesc=desc)
        d.save()
        context={'success':True}
        
    return render(request,'home.html',context)


def task(request):
    alltasks = Task.objects.all()
    context={'tasks':alltasks}
    return render(request,'task.html',context)

def remove(request,item_id):
    item=Task.objects.get(id=item_id)
    item.delete()
    return redirect("tasks")    

def update(request,item_id):
    item=Task.objects.get(id=item_id)
    if request.method == "POST":
        item.TaskDesc = request.POST['desc']
        item.save()
        return redirect("tasks")
    else:
        context={'id':item_id,'title':item.TaskTitle,'desc':item.TaskDesc}
        return render(request,'update.html',context)
    
    