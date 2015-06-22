from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader, RequestContext
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = RequestContext(request, {
        "latest_questions": latest_questions
    })
    return HttpResponse(template.render(context))
    # output = ", ".join([q.question_text for q in latest_questions])
    # return HttpResponse(output)
    # return HttpResponse("Hello ,world.You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at the question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
