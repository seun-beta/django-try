from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render
from django.views import View

def index(request):
    return HttpResponse('''Hello, world. You're at the polls index.
    It is great to have you here. This is one of my Django apps''')

class GameView(View):
    def get(self, request, guess):
        x = {'guess':int(guess)}
        return render(request, 'polls/cond.html', x)


class ChoiceView(View):
    def get(self, request, option):
        a = {'option':int(option)}
        return render(request, 'polls/choice.html', a)


class DangerView(View):
    def get(self, request, input):
        b = {'input': input}
        return render(request, 'polls/danger.html', b)

def simple(request):
    return render(request, 'polls/simple.html')

def guess(request):
    context = {'guess':45}
    return render(request, 'polls/guess.html', context)

def special(request):
    ctx = { 'special1':12,
            'special2' : '<b> Bold </b>',
            'special3' : '<b> Bold </b>'
    }
    return render(request, 'polls/special.html', ctx)

def nuts(request):
    f = ['Apple', 'Orange', 'Pawpaw', 'Kiwi']
    n = ['cashewnut', 'pistachio', 'groundnut']
    ctx = {'fruits': f, 'nuts' : n, 'zap' : 42 }
    return render(request, 'polls/nuts.html', ctx)

def loop(request):
    ctx = {'loop':[1,2,3,4,5]}
    return render(request, 'polls/loop.html', ctx)

def nested(request):
    ctx = { 'outer': {'inner' : 1360 }}
    return render(request, 'polls/nested.html', ctx)

def nested_objects(request):
    ctx = {'outer': {'inner': [1,2,3,4,5]}}
    return render(request, 'polls/nested_objects.html', ctx)


class Inheritance1(View):
    def get(self, request):
        ctx = {'inheritance1':'This is Inheritance 1'}
        return render(request, 'polls/inheritance1.html', ctx)

class Inheritance2(View):
    def get(self, request):
        ctx = {'inheritance2': 'This is Inheritance 2'} 
        return render(request, 'polls/inheritance2.html', ctx)

def urlmap(request):
    return render (request, 'polls/url1.html')
