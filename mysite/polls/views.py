from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    results = "You're looking at the results of question %s."
    return HttpResponse(results % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on %s." % question_id)