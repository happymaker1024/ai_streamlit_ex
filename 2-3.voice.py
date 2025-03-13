####### lib 설치 ##########
# pip install openai
# pip install streamlit
# pip install python-dotenv
###########################
# 실행 : streamlit run 2-3.voice.py
###########################
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

import os

# .env 파일 경로 지정, 환경변수 로딩 
load_dotenv(override=True)
# load_dotenv(dotenv_path=".env.dev", override=True)

# Open AI API 키 설정하기
# api_key 변수에 OPENAI_API_KEY 대입
api_key = os.getenv('OPENAI_API_KEY')
# print(api_key)

# OpenAI Key 값 셋팅
# OpenAI 객체생성, client변수에 대입
# client <- 객체변수
client = OpenAI(api_key = api_key)
# -------------- 여기 환경셋팅 ----------------

# 뷰포트에 h1 태그로 텍스트 출력
st.title("OpenAI's Text-to-Audio Response")

# url 이미지를 뷰포트에 표시 width 200px
st.image("https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%84%B1%EC%9A%B0.jpg", width=200)

# 인공지능 성우 선택 박스를 생성.
# 공식 문서 참고: https://platform.openai.com/docs/guides/text-to-speech
# 인공지능 목소리 목록
options = ['alloy', 'ash', 'coral', 'echo', 'fable', 'onyx', 'nova', 'sage', 'shimmer']

# 뷰포트에 선택목록을 표시하고, 사용자가 선택하면, selected_option 변수에 저장
selected_option = st.selectbox("성우를 선택하세요:", options)

# 문자열 default_text 변수에 대입
default_text = '오늘은 생활의 꿀팁을 알아보겠습니다.'
# 텍스트박스 표시, 레이블 출력, 초기값 출력 
# 사용자가 값을 입력하면 user_prompt에 대입
user_prompt = st.text_area("인공지능 성우가 읽을 스크립트를 입력해주세요.", value=default_text, height=200)

# 버튼 표시
# st.button("Generate Audio")

# Generate Audio 버튼을 클릭하면 True가 되면서 if문 실행.
if st.button("Generate Audio"):

    # 텍스트로부터 음성을 생성.
    # selected_option, user_prompt 값으로 tts-1 모델에 음성생성요청
    # 응답을 audio_response에 저장
    audio_response = client.audio.speech.create(
        model="tts-1",
        voice=selected_option,
        input=user_prompt,
    )

    # 리턴값에서 오디오만 추출
    audio_content = audio_response.content

    # 음성을 mp3 파일로 저장
    # 바이너리로 쓰겠다(음성데이터), audio_file : 파일변수
    with open("temp_audio.mp3", "wb") as audio_file:
        # audio_content 저장된 값을 오디오 파일로 저장
        audio_file.write(audio_content)

    # audio 컨트롤러 표시, mp3 파일을 재생 가능
    st.audio("temp_audio.mp3", format="audio/mp3")