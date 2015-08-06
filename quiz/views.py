from django.shortcuts import render
# coding: utf-8
# Create your views here.
quizzes = {
	"myborjeson": {
   		"name": u"My quiz",
	   	"description": u"How well do you know me?"
	},
	"fotboll": {
	   	"name": u"Största fotbollslagen",
	   	"description": u"Kan du dina lag?"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
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

def question(request, slug, number):
	context = {
		"question_number": number,
		"question": u"Hur många bultar har Ölandsbron?",
		"answer1": "12",
		"answer2": "66 400",
		"answer3": "7 428 495",
		"quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)
#def questiontwo(request):
#	return render(request, "quiz/questiontwo.html")
def completed(request):
	return render(request, "quiz/completed.html")
