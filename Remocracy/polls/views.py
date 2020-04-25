from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.


# def detail(request,questionID):
# 	question = get_object_or_404(Question,pk=questionID)
# 	context = {
# 		'question':question
# 	}
# 	return render(request,'polls/detail.html',context)

# def results(request,questionID):
# 	response = f"You're looking at the results of question {questionID}<br>"
# 	question = get_object_or_404(Question,pk=questionID)
# 	context = {
# 		'question':question
# 	}
# 	return render(request,'polls/results.html',context)

# def IndexView(generic.ListView):
# 	latestQuestions = Question.objects.order_by('-pubDate')[:5]
# 	context = {
# 		'latestQuestions':latestQuestions
# 	}
# 	return render(request,'polls/index.html',context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,questionID):
	question = get_object_or_404(Question,pk=questionID)
	try:
		selectedChoice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		context = {
			'question':question,
			'error_message':'SELECT A CHOICE YOU STUPID IDIOT'
		}
		return render(request,'polls/detail.html',context)
	else:
		selectedChoice.votes += 1
		selectedChoice.save()
		return HttpResponseRedirect(reverse('results',args=(question.id,)))

