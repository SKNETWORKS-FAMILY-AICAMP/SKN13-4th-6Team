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
    
    # LLM이 사용자 의도를 판단하도록 함
    def classify_user_intent(user_message):
        """사용자 메시지가 카드 추천 요청인지 일반 대화인지 LLM이 판단"""
        classification_prompt = f"""
다음 사용자 메시지가 신용카드 추천을 요청하는 것인지, 일반적인 대화인지 판단해주세요.
특정 카테고리의 카드를 추천해달라는 요청이 아닌 경우에는 일반 대화라고 판단하세요.

사용자 메시지: "{user_message}"

카드 추천 요청의 예시:
- "주유 할인 카드 추천해줘"
- "외식 혜택 좋은 카드 있어?"
- "연회비 없는 카드 찾고 있어"
- "대학생이 쓰기 좋은 카드 추천해줘"
- "마일리지 적립 잘 되는 카드"
- "커플이 같이 쓰기 좋은 카드"

일반 대화의 예시:
- "안녕하세요"
- "날씨가 좋네요"
- "고마워요"
- "뭐해?"
- "잘 있어"
- "어떤 종류의 카드를 추천해줄 수 있어?"

답변은 반드시 다음 중 하나로만 해주세요:
- "CARD_RECOMMENDATION" (카드 추천 요청인 경우)
- "GENERAL_CHAT" (일반 대화인 경우)
"""
        
        try:
            llm = recommendation_system.model_manager.llm
            response = llm.invoke(classification_prompt)
            result = response.content.strip().upper()
            
            if "CARD_RECOMMENDATION" in result:
                return True
            else:
                return False
        except:
            # LLM 호출 실패 시 기본적으로 일반 대화로 처리
            return False
    
    is_card_related = classify_user_intent(message)
    
    try:
        # 스트리밍 응답 생성
        def generate_response():
            try:
                # LLM에서 스트리밍 응답 받기
                llm = recommendation_system.model_manager.llm
                if not llm:
                    yield f"data: {json.dumps({'response': '모델이 초기화되지 않았습니다.'})}\n\n"
                    return
                
                from recommendation.prompt_builder import PromptBuilder
                
                if is_card_related:
                    # 카드 추천 관련 메시지인 경우
                    query = message
                    docs_data = recommendation_system._retrieve_and_filter_docs(query)
                    formatted_data = recommendation_system._format_docs_for_prompt(docs_data)
                    
                    # 카드 추천 프롬프트 생성
                    prompt = PromptBuilder.create_recommendation_prompt()
                    formatted_prompt = prompt.format(**formatted_data)
                else:
                    # 일반 대화인 경우
                    prompt = PromptBuilder.create_general_chat_prompt()
                    formatted_prompt = prompt.format(question=message)
                
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
                error_msg = f"응답 중 오류가 발생했습니다: {str(e)}"
                yield f"data: {json.dumps({'response': error_msg})}\n\n"
        
        return StreamingHttpResponse(
            generate_response(),
            content_type='text/plain'
        )
        
    except Exception as e:
        return JsonResponse({"response": f"오류가 발생했습니다: {str(e)}", "received_message": message})