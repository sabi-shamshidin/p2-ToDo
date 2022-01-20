from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class List(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.all()
        context = {'tasks': tasks}
        return context


class Create(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Create, self).form_valid(form)
