from django.shortcuts import render, redirect
from .models import Task

tasks = ["Finish work", "study Django"]

def home(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        task = Task.objects.create(title=title)
        task.save()
        return redirect('home')

def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.filter(id=id).first()
        if task:
            task.delete()
    return redirect('home')

def view_task(request, id):
    task = Task.objects.filter(id=id).first()
    if not task:
        return render(request, 'tasks/not_found.html', status=404)
    return render(request, 'tasks/view_task.html', {'task': task})

def edit_task(request, id):
    task = Task.objects.filter(id=id).first()
    if not task:
        return render(request, 'tasks/not_found.html', status=404)

    if request.method == 'POST':
        task.title = request.POST.get('task')
        task.save()
        return redirect('home')

    return render(request, 'tasks/edit_task.html', {'task': task, 'id': task.id})
