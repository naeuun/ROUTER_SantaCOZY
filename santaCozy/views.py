from django.shortcuts import render

def index(request):
    return render(request, 'santaCozy/index.html')

def loading(request):
    return render(request, 'santaCozy/loading.html')

def result(request):
    return render(request, 'santaCozy/result.html')
