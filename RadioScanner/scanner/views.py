from scanner import models

def index(request):
	processTable()
	return HttpResponse("Hello, world. You're at the poll index.")
