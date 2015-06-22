from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.
from django.template import loader, RequestContext
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]

    # shortcut:render
    context = {
        "latest_questions": latest_questions
    }
    return render(request, "polls/index.html", context)

    # # template,context and rendering
    # template = loader.get_template("polls/index.html")
    # context = RequestContext(request, {
    #     "latest_questions": latest_questions
    # })
    # return HttpResponse(template.render(context))

    # # output by hard-coding
    # output = ", ".join([q.question_text for q in latest_questions])
    # return HttpResponse(output)

    # return HttpResponse("Hello ,world.You're at the polls index.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("You're looking at the question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
