# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from recommendation.recommender import get_recommendation_system
recommendation_system = get_recommendation_system()

def chat_interface(request):
    return render(request, 'chatbot/chat.html')

def chat_api(request):
    message = request.GET.get("message", "")
    
    if not message:
        return JsonResponse({"response": "메시지를 입력해주세요.", "received_message": ""})
    
    try:
        # 스트리밍 응답 생성
        def generate_response():
            try:
                # LLM에서 스트리밍 응답 받기
                llm = recommendation_system.model_manager.llm
                if not llm:
                    yield f"data: {json.dumps({'response': '모델이 초기화되지 않았습니다.'})}\n\n"
                    return
                
                # RAG 체인의 마지막 단계(LLM)만 스트리밍으로 실행
                query = message
                docs_data = recommendation_system._retrieve_and_filter_docs(query)
                formatted_data = recommendation_system._format_docs_for_prompt(docs_data)
                
                # 프롬프트 생성
                from recommendation.prompt_builder import PromptBuilder
                prompt = PromptBuilder.create_recommendation_prompt()
                formatted_prompt = prompt.format(**formatted_data)
                
                # 스트리밍 응답 처리
                response_text = ""
                for chunk in llm.stream(formatted_prompt):
                    if hasattr(chunk, 'content'):
                        content = str(chunk.content)
                        response_text += content
                        yield f"data: {json.dumps({'response': response_text})}\n\n"
                
                # 완료 신호
                yield "data: [DONE]\n\n"
                
            except Exception as e:
                error_msg = f"추천 중 오류가 발생했습니다: {str(e)}"
                yield f"data: {json.dumps({'response': error_msg})}\n\n"
        
        return StreamingHttpResponse(
            generate_response(),
            content_type='text/plain'
        )
        
    except Exception as e:
        return JsonResponse({"response": f"오류가 발생했습니다: {str(e)}", "received_message": message})