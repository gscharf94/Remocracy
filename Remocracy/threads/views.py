from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Thread

# Create your views here.
def index(request):
	threadList = Thread.objects.all()
	index = 'index'
	context = {
		'threadList':threadList,
		'index':index,
	}
	return render(request,'threads/index.html',context)

def detailThread(request,threadID):
	thread = Thread.objects.get(pk=threadID)
	context = {
		'thread':thread
	}
	return render(request,'threads/detailThread.html',context)

def voteUpThreadFromIndex(request,threadID):
	thread = Thread.objects.get(pk=threadID)
	thread.votes += 1
	thread.save()
	return redirect('index')

def voteDownThreadFromIndex(request,threadID):
	thread = Thread.objects.get(pk=threadID)
	thread.votes += -1
	thread.save()
	return redirect('index')
