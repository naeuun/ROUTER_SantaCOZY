from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.urls import reverse
import google.generativeai as genai
from .utils import call_gemini_api

def get_429_popup_html():
    error_message = "접속량이 많아 코지가 지쳤어요.. 다음에 접속해주세요"
    index_url = reverse("santaCozy:index") 
    # ... (HTML 내용 유지) ...
    html_content = f"""
    <html>
    <head>
        <title>요청 과부하 오류</title>
    </head>
    <body>
        <script>
            alert('{error_message}');
            window.location.href = '{index_url}'; 
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content, status=429)

def index(request):
    return render(request, 'santaCozy/index.html')

def loading(request):
    if request.method == "POST":
        worry = request.POST.get("worry")

        if not worry:
            return render(request, "santaCozy/index.html", {"error": "고민을 입력해주세요!"})

        return render(request, "santaCozy/loading.html", {"worry": worry})


def result(request):
    if request.method == "POST":
        worry = request.POST.get("worry")
        
        try:
            answer = call_gemini_api(worry)
            return render(request, "santaCozy/result.html", {"answer": answer})
        
        except Exception as e:
            error_message = str(e).lower()

            if '429' in error_message or 'exhausted' in error_message or 'quota' in error_message:
                return get_429_popup_html()

            raise e 

    return redirect("santaCozy:index")