from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')

def cuerpodocente(request):
	return render(request, 'miapp/cuerpodocente.html')

def gunsnroses(request):
	return render(request, 'miapp/gunsnroses.html')