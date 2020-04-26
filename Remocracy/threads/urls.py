from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('<int:threadID>/',views.detailThread,name='detailThread'),
	path('votethr/<int:threadID>/<str:howMuch>/<str:fromWhere>',views.voteThread,name='voteThread'),
	path('votecom/<int:threadID>/<int:commentID>/<str:howMuch>/',views.voteComment,name='voteComment'),
	path('login/',auth_views.LoginView.as_view(template_name='threads/login.html'),name='login'),
	path('login/profile',views.userProfile,name='userProfile'),
]