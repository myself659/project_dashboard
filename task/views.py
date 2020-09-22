from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
   return HttpResponse("Welcome to Simple Project Dashboard")

from django.views.generic import ListView
from .models import Task 

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.utils import timezone

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name','task_desc']
    success_url = '/task_list'
    extra_context = {
        'title': 'Create Task'
    }
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    def form_valid(self, form):
        form.instance.task_creator = self.request.user
        form.instance.task_created = timezone.now
        return super().form_valid(form)