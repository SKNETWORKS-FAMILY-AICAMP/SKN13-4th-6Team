# SKN13-4th-6TEAM

## 팀원 소개
<table align=center>
  <tbody>
   <tr>
      <td align=center><b>최성장</b></td>
      <td align=center><b>고범석</b></td>
      <td align=center><b>김동욱</b></td>
      <td align=center><b>안수민</b></td>
      <td align=center><b>지형우</b></td>
    </tr>
    <tr>
      <td align="center">
          <img alt="Image" src="images\마이멜로디1.jpg" width="200px;" alt="최성장"/>
      </td>
      <td align="center">
          <img alt="Image" src="images\마이멜로디1.jpg" width="200px;" alt="고범석"/>
      </td>
      <td align="center">
          <img alt="Image" src="images\마이멜로디1.jpg" width="200px;" alt="김동욱"/>
      </td>
      <td align="center">
        <img alt="Image" src="images\마이멜로디1.jpg" width="200px;" alt="안수민" />
      </td>
      <td align="center">
        <img alt="Image" src="images\마이멜로디1.jpg" width="200px;" alt="지형우"/>
      </td>
    </tr>
    <tr>
        <td align="center">
       <a href="https://github.com/GrowingChoi">
         <img src="https://img.shields.io/badge/GitHub-GrowingChoi-BD9FFF?logo=github" alt="최성장 GitHub"/>
       </a>
       </td>
       <td align="center">
       <a href="https://github.com/qjazk0000">
         <img src="https://img.shields.io/badge/GitHub-qjazk0000-BD9FFF?logo=github" alt="고범석 GitHub"/>
       </a>
       </td>
       <td align="center">
       <a href="https://github.com/boogiewooki02">
         <img src="https://img.shields.io/badge/GitHub-boogiewooki02-BD9FFF?logo=github" alt="김동욱 GitHub"/>
       </a>
       <td align="center">
       <a href="https://github.com/tnalsdk111">
         <img src="https://img.shields.io/badge/GitHub-tnalsdk111-BD9FFF?logo=github" alt="안수민 GitHub"/>
       </a>
       </td>
       </td>
       <td align="center">
       <a href="https://github.com/JI0617">
         <img src="https://img.shields.io/badge/GitHub-JI0617-BD9FFF?logo=github" alt="지형우 GitHub"/>
       </a>
       </td>
    </tr>
  </tbody>
</table>
<br>
<br/><br/>


## 프로젝트 개요

사용자의 소비 성향과 원하는 혜택에 따라 최적의 신용카드를 추천하는 RAG 기반 AI 챗봇입니다.  
질문 한 줄만으로 방대한 카드 혜택 정보를 요약하고 비교해, 빠르고 정확한 카드 선택을 돕습니다.

### 프로젝트 필요성

수많은 카드사와 혜택이 혼재된 시장에서 소비자는 자신에게 맞는 카드를 찾기 어려운 상황입니다.  
공식 홈페이지나 블로그, 광고 정보는 분산되어 있어 객관적인 비교가 어렵고, 소비자 입장에서 실질적인 정보 접근성도 낮습니다.  
특히 특정 혜택(예: 주유, 해외 결제, 스트리밍 할인 등)을 중점적으로 비교하고자 할 때, 신뢰할 수 있는 정보 제공 시스템의 부재가 문제가 되고 있습니다.

이에 따라, 신용카드 혜택 정보를 통합 수집하고 사용자의 질문에 맞춰 맞춤형으로 추천해주는 AI 기반 챗봇의 필요성이 대두되고 있습니다.

### 프로젝트 목표

- 카드 혜택, 연회비, 발급 조건 등 다양한 정보를 통합적으로 제공하는 신용카드 추천 챗봇을 구축합니다.  
- RAG(Retrieval-Augmented Generation) 구조를 기반으로, 문서 검색과 LLM 응답 생성을 결합하여 사용자 질문에 정확한 답변을 제공합니다.  
- LangChain 기반 파이프라인을 통해 크롤링, 전처리, 벡터화, 검색, 응답 생성을 체계화하고, RAGAS 지표를 활용해 성능을 정량적으로 평가합니다.  
- 사용자 신뢰도 확보를 위해 카드 상세 페이지 링크와 혜택 출처 정보를 함께 제공합니다.  
- 누구나 쉽게 접근 가능한 웹 인터페이스와 챗봇 구조를 통해 카드 정보 탐색의 진입 장벽을 낮추고, 소비자 선택을 돕습니다.

## 시스템 아키텍쳐
```
chat_project/
├── chat_project/     
│   ├── __init__.py               
│   ├── asgi.py   
│   ├── settings.py                  
│   ├── urls.py                  
│   └── wsgi.py
├── accounts/                   
│   ├── __init__.py
│   ├── admin.py    
│   ├── apps.py          
│   ├── forms.py          
│   ├── models.py          
│   ├── tests.py          
│   ├── urls.py          
│   └── views.py
├── chatbot/                  
│   ├── __init__.py    
│   ├── admin.py    
│   ├── apps.py          
│   ├── models.py          
│   ├── tests.py          
│   ├── urls.py          
│   └──views.py          
├── recommendation/              
│   ├── model_manager.py        
│   ├── query_filter.py        
│   ├── formatter.py            
│   ├── prompt_builder.py       
│   ├── recommender.py          
│   ├── apps.py        
│   └── __init__.py
├── templates/                  
│   └── base.html   
├── manage.py   
├── db.sqlite3
├── documents/              
│   ├── 요구사항 명세서        
│   ├── 화면 설계서     
│   ├── 시스템 구성도                
│   └── 테스트 계획서 및 테스트 결과 보고서
└── README.md          
```
