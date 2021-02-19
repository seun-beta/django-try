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
    response = """
        <body>
        <p>
            GET Request Example
        </p>
        <form action="" method="GET">
            <label for="guess">   Input your guess   </label>
            <input type="text" name="guess" id="guess">
            <input type="submit" value="Submit">
        </form>
        </body>                      
    """
    response = response + dumpdata('GET', request.GET)
    return HttpResponse(response)

@csrf_exempt
def postform(request):
    response = """
        <body>
        <p>
            POST Request Example
        </p>
        <form action="" method="POST">
            <label for="guess">   Input your guess   </label>
            <input type="text" name="guess" id="guess">
            <input type="submit" value="Submit">
        </form>
        </body>             
    """
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

def get_try(request):
    response = """
        <body>
        <p>
            This is an example of a GET 
        </p>
        <form action="" method="GET">
            <label for="guess">   Input your number:   </label></br>
            <input type="text" name="guess" id="guess">
            <input type="submit" value="Submit">
        </form>
        </body>             
    """
    return HttpResponse(response)

@csrf_exempt
def post_try(request):
    response = """
        <body>
        <p>
            This is an example of a POST 
        </p>
        <form action="" method="POST">
            <label for="guess">   Input your guess:   </label></br>
            <input type="text" name="guess" id="guess">
            <input type="submit" value="Submit">
        </form>
        </body>             
    """
    return HttpResponse(response)
