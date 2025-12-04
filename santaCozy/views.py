from django.shortcuts import redirect, render
from .utils import call_gemini_api

def index(request):
    return render(request, 'santaCozy/index.html')

def loading(request):
    if request.method == "POST":
        worry = request.POST.get("worry")

        if not worry:
            return render(request, "santaCozy/index.html", {
                "error": "고민을 입력해주세요!"
            })

        return render(request, "santaCozy/loading.html", {"worry": worry})

def result(request):
    if request.method == "POST":
        worry = request.POST.get("worry")
        
        answer = call_gemini_api(worry)

        return render(request, "santaCozy/result.html", {
            "answer": answer
        })

    return redirect("santaCozy:index")
