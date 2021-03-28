from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import FriendForm
from .forms import FindForm
from .forms import Friend
from .models import Friend
from django.shortcuts import redirect

def index(request):
    data = Friend.objects.all()
    params = {
            'title': 'Hello',
            'data': data,
    }

    return render(request, 'db_training/index.html', params)


def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance = obj)
        friend.save()
        return redirect(to='/training')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }   
    return render(request, 'db_training/create.html', params)


def edit(request, num): #numでURLで指定された
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/training')
    
    params = {
        'title': 'Hello',
        'id':  num, #int型だからクオーテつけんな
        'form': FriendForm(instance=obj)

    }
    return render(request, 'db_training/edit.html', params)


def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/training')
    
    params = {
        'title' : 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'db_training/delete.html', params)

def find(request):
    if(request.method == 'POST'):
        msg = '結果'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Friend.objects.filter(name__contains=str)
    else:
        msg = 'なにさがしてるん'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': 'msg',
        'data': data,
        'form': form
    }
    return render(request, 'db_training/find.html', params)


        

