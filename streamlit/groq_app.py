import streamlit as st
import requests

# Groq API를 호출하는 함수 정의
def get_groq_response(user_input):
    # Groq API 엔드포인트와 인증키 설정
    api_url = "https://api.groq.com/openai/v1/models"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "prompt": user_input,
        "max_tokens": 50
    }

    # API 요청
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['text']
    else:
        return "응답을 가져오는 데 실패했습니다."

# Streamlit 앱 구성
st.title("챗봇")
st.subheader("Groq와 함께하는 간단한 챗봇")

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:")

# 버튼 클릭 시 응답 가져오기
if st.button("전송"):
    if user_input:
        bot_response = get_groq_response(user_input)
        st.text_area("챗봇 응답:", value=bot_response, height=100, max_chars=300, key="response")
    else:
        st.warning("질문을 입력해 주시기 바랍니다.")
