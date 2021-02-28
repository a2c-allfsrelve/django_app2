from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PullDown

class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'result': None,
            'form': PullDown(),
        }
    
    def get(self, request):
        return render(request, 'db_training/index.html', self.params)

    def post(self, request):
        ch = request.POST['choise']
        self.params['result'] = 'selected : ' + ch
        self.params['form'] = PullDown(request.POST)
        return render(request, 'db_training/index.html', self.params)