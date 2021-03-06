from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from quiz import views
urlpatterns = [
    url("^$", views.startpage, name="start_page"),
	url(r"^quiz/([A-Za-z-]+)/$", views.quiz, name="quiz_page"),
	url(r"^quiz/([A-Za-z-]+)/question/([0-9]+)/$", views.question, name="question_page"),
	url(r"^quiz/([A-Za-z-]+)/completed/$", views.completed, name="completed_page"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^pages/', include('django.contrib.flatpages.urls')),
]