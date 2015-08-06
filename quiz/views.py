from django.shortcuts import render

# Create your views here.
def startpage(request):
return render(request, "quiz/templates/startpage.html")
def quiz(request):
return render(request, "quiz/templates/start-quiz.html")
def questionone(request):
return render(request, "quiz/templates/questionone.html")
def questiontwo(request):
return render(request, "quiz/templates/questiontwo.html")
def result(request):
return render(request, "quiz/templates/resultpage.html")
