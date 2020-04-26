from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('<int:threadID>/',views.detailThread,name='detailThread'),
	path('<int:threadID>/voteup/',views.voteUpThreadFromIndex,name='voteUpThreadFromIndex'),
	path('<int:threadID>/votedown/',views.voteDownThreadFromIndex,name='voteDownThreadFromIndex'),
]