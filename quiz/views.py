from django.shortcuts import render
# coding: utf-8
# Create your views here.
quizzes = {
	"my": {
   		"name": u"My quiz",
	   	"description": u"How well do you know me?"
	},
}

def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html",context)
def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request):
	return render(request, "quiz/question.html")
#def questiontwo(request):
#	return render(request, "quiz/questiontwo.html")
def completed(request):
	return render(request, "quiz/completed.html")
