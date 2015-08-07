# endcoding: utf-8
from django.shortcuts import render
from quiz.models import Quiz

def startpage(request):
	context = {
	    "quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html",context)

def quiz(request, slug):
	context = {
	    	"quiz": Quiz.objects.get(slug=slug),
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
def completed(request, slug):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/completed.html", context)
