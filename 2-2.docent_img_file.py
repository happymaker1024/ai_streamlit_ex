####### lib 설치 ##########
# pip install openai
# pip install streamlit
# pip install python-dotenv
###########################
# 실행 : streamlit run 2-2.docent_img_file.py
###########################

import base64
from io import BytesIO
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image  # PIL 라이브러리 필요

# .env 파일 로드
load_dotenv(override=True)

# Open AI API 키 설정
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# 이미지를 Base64로 변환하는 함수
# Base64 인코딩은 바이너리 데이터를 ASCII 문자열로 변환하는 표준 방식
def encode_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")  # PNG 형식으로 변환
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# 이미지 파일을 분석하여 설명을 반환하는 함수
def ai_describe(image):
    try:
        base64_image = encode_image(image)  # 이미지를 Base64로 변환
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "이 이미지에 대해서 자세하게 설명해 주세요."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
                    ],
                }
            ],
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"오류 발생: {str(e)}"

# 웹 앱 UI 설정
st.title("AI 도슨트: 이미지를 설명해드려요!")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 업로드된 이미지 표시
    st.image(uploaded_file, width=300)
    
    # 이미지 설명 요청 버튼
    if st.button("해설"):
        image = Image.open(uploaded_file)  # PIL 이미지 열기
        
        # GPT-4V를 이용한 이미지 분석 수행
        result = ai_describe(image)
        st.success(result)
