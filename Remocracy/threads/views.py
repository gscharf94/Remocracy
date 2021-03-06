from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Thread, Comment

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
	comments = thread.comment_set.all()
	context = {
		'thread':thread,
		'comments':comments
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

def voteThread(request,threadID,howMuch,fromWhere):
	thread = Thread.objects.get(pk=threadID)
	thread.votes += int(howMuch)
	thread.siteUser.votes += int(howMuch)
	thread.siteUser.save()
	thread.save()
	if fromWhere == 'detail':
		return redirect('detailThread',threadID)
	elif fromWhere == 'index':
		return redirect('index')

def voteComment(request,threadID,commentID,howMuch):
	thread = Thread.objects.get(pk=threadID)
	comment = Comment.objects.get(pk=commentID)
	comment.votes += int(howMuch)
	comment.siteUser.votes += int(howMuch)
	comment.siteUser.save()
	comment.save()
	return redirect('detailThread',threadID)

def userProfile(request):
	try:
		currentUser = request.user
		siteUser = currentUser.siteuser
		context = {
			'currentUser':currentUser,
			'siteUser':siteUser,
		}
		return render(request,'threads/userProfile.html',context)
	except:
		context = {

		}
		return render(request,'threads/noUserProfile.html',context)

def submitThread(request):
	context = {

	}
	return render(request,'threads/submitThread.html',context)