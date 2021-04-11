from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import FriendForm
from .forms import FindForm
from .forms import Friend
from .models import Friend
from django.shortcuts import redirect
from django.db.models import Count, Sum, Avg, Min, Max
from .forms import CheckForm

def index(request):
    data = Friend.objects.all().order_by('id')
    re1 = Friend.objects.aggregate(Count('age'))
    re2 = Friend.objects.aggregate(Sum('age'))
    re3 = Friend.objects.aggregate(Avg('age'))
    re4 = Friend.objects.aggregate(Min('age'))
    re5 = Friend.objects.aggregate(Max('age'))
    msg = 'count:' + str(re1['age__count']) \
        +'<br>Sum:' + str(re2['age__sum']) \
        +'<br>Average:' + str(re3['age__avg']) \
        +'<br>Min:' + str(re4['age__min']) \
        +'<br>Max:' + str(re5['age__max']) 

    params = {
            'title': 'Hello',
            'message': msg,
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
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'SELECT * FROM db_training_friend'
        if (msg != ''):
            sql += ' WHERE ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
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


def check(request):
    params = {
        'title': 'Hello',
        'message': 'ばりでーしょん',
        'form': FriendForm(),
        
        
    }
    if(request.method == 'POST'):
        # form = CheckForm(request.POST)

        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if(form.is_valid()):
            params['message'] = 'OK'
        else:
            params['message'] = 'no good'
        
    return render(request, 'db_training/check.html', params)
    





        

