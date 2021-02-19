from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils import html
from django.views import View
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

def dumpdata(label, data):
    retval = ''
    if len(data) > 0 :
        retval = retval + '<p>Incoming '+ label + ' data:</br>\n'
        for key, value in data.items():
            retval = retval +  html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'

    return retval

def getform(request):
    return render(request, 'polls/getform.html')

def postform(request):
    return render(request, template_name='polls/postform.html')

def get_try(request):
    return render(request, 'polls/get_try.html')


def post_try(request):
    return render(request, 'polls/post_try.html')

def checkguess(guess):
    try:
        if int(guess) < 10 :
            msg = 'Guess is too low'
        elif int(guess) == 10 :
            msg = 'You got it!'
        else:
            msg = 'Your guess is too high'
    except:
        msg = 'Your guess was invalid: ' + guess

    return msg


def guess_try(request, guess):
    msg = checkguess(guess)
    context = {'guess' : msg}
    return render(request, 'polls/guess_try.html', context)

class GuessView(View):
    def get(self, request, guess):
        return render(request, 'polls/guess.html')

    def post(self, request, guess):
        guess = request.POST.get('guess')
        msg = checkguess(guess)
        return render(request, 'polls/guess.html', {'message': msg})
