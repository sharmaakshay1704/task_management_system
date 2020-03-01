from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItems

def todoapp(request):
    alltodoitems=TodoItems.objects.all()
    return render(request,'todo.html',{'allitems':alltodoitems})

def todoadd(request):
    new_items=TodoItems(content=request.POST['content'])
    new_items.save()
    return HttpResponseRedirect('/')

def tododelete(request,todoid):
    itemtodelete=TodoItems.objects.get(id=todoid)
    itemtodelete.delete()
    return HttpResponseRedirect('/')
    