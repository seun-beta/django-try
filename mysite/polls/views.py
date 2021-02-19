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

@csrf_exempt
def postform(request):
    return render(request, template_name='polls/postform.html')

def get_try(request):
    return render(request, 'polls/get_try.html')


def post_try(request):
    return render(request, 'polls/post_try.html')