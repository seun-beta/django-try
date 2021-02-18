from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    ctx = {'latest_question_list' : latest_question_list,}
    return render(request, 'polls/index.html', ctx)

def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        ctx = {'question', question}
        return render(request, 'polls/detail.html', ctx )

def results(request, question_id):
    response = ("You're looking at the results of question %s.")
    return HttpResponse(response % question_id )

def vote(request, question_id):
    return HttpResponse("You're voting on question  %s" %question_id)

def cookie_try(request):
    print(request.COOKIES)
    resp = HttpResponse('Welcome to my cookies page')
    resp.set_cookie('billie', 365)
    resp.set_cookie('jean', 366, max_age=200)
    return (resp)