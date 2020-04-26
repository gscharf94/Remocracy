from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('<int:threadID>/',views.detailThread,name='detailThread'),
	path('votethr/<int:threadID>/<str:howMuch>/<str:fromWhere>',views.voteThread,name='voteThread'),
	path('votecom/<int:threadID>/<int:commentID>/<str:howMuch>/',views.voteComment,name='voteComment')
]