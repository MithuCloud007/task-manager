from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/all.html'
    
class TaskAdd(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add.html'
    success_url= reverse_lazy('tasks:all_tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url= reverse_lazy('tasks:all_tasks') 
    
    
class TaskView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/view.html' 
    
class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/tasks_confirm_delete.html' 
    success_url= reverse_lazy('tasks:all_tasks')                     