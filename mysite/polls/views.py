from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from django.template import loader, RequestContext
from django.views import generic
from django.utils import timezone
from .models import Question, Choice


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    #
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


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_questions"

    def get_queryset(self):
        """Returns the last five published questions."""
        # return Question.objects.order_by("-pub_date")[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
        ).order_by("-pub_date")[:5]


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("You're looking at the question %s." % question_id)


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
    # response = "You're looking at the results of question %s." % question_id
    # return HttpResponse(response)


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (Choice.DoesNotExist, KeyError):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # return HttpResponse("You're voting on question %s." % question_id)
