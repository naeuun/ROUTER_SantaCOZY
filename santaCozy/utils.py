import google.generativeai as genai
from django.conf import settings

def call_gemini_api(worry):
    genai.configure(api_key=settings.GEMINI_API_KEY)

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-lite",
        system_instruction=(
            "사용자가 입력한 고민에 대해 충고 없이 조언, 위로, 격려, 지지, 응원의 말을 해줘! "
            "고민 내용이나 학생 정보를 다시 언급하지 마."
            "3~4줄 정도로 성의 있게 한국어로 답변하는데, 반드시 존댓말을 사용해서 따뜻한 말투로 답변해"
        )
    )

    prompt = worry

    response = model.generate_content(prompt)

    return response.text
