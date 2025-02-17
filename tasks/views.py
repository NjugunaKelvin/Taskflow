from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks' : tasks})