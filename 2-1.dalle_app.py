import streamlit as st

# 1. 사용자에게 보여지는 부분 구현
# - 타이틀
st.title("그림 그리는 AI 화가 서비스 🌸")
# - 이미지표시
st.image("images/robot_painter.jpg", caption="로봇 화가")

# - 설명 텍스트 출력
st.write("원하는 그림을 말해주세요. 그려드리겠습니다.")
st.write("원하는 이미지의 설명을 영어로 적어보세요.")
# - textarea : 영어로 그림그리기 설명 프롬프트 입력
text = st.text_area("")
# - 버튼 : 그림을 요청하기 gtp에게
st.button("Painting")
