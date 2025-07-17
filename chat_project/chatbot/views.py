# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse
from recommendation.recommender import get_recommendation_system
recommendation_system = get_recommendation_system()

def chat_interface(request):
    return render(request, 'chatbot/chat.html')

def chat_api(request):
    message = request.GET.get("message", "")
    try:
        response_text = recommendation_system.recommend_cards(message)
    except Exception as e:
        response_text = f"추천 중 오류가 발생했습니다: {e}"

    return JsonResponse({"response": response_text, "received_message": message})