from django.shortcuts import render
from .models import Tasks


def todo(request):
    todos_list = Tasks.objects.all()
    context = {'todos_list': todos_list}
    return render(request, 'home/view.html', context=context)
