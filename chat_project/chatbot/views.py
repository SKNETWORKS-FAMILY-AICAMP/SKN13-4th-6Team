from django.shortcuts import render
from django.http import JsonResponse

def chat_interface(request):
    return render(request, 'chatbot/chat.html')

def chat_api(request, message):
    # 이 부분에 실제 챗봇 응답 로직을 넣으면 됨. (필요시 파일 분리)
    # 지금은 임시 응답만 반환.
    
    response = f"'{message}'에 대한 응답입니다."  # 실제로 LLM에서 생성된 결과로 교체해야 함.
    return JsonResponse({'response': response})
