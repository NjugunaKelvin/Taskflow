from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks' : tasks})


@login_required
def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('task_list')
    
    return render(request, 'tasks/task_form.html')
    

@login_required
def task_delete(request, pk):  # Add 'pk' parameter here
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if not title:
            messages.error(request, 'Title is required!')
            return render(request, 'tasks/task_form.html', {'task': task})
        
        task.title = title.strip()
        task.description = description.strip() if description else ''
        task.save()
        
        messages.success(request, 'Task updated successfully!')
        return redirect('task_list')
    
    return render(request, 'tasks/task_form.html', {'task': task})




def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')