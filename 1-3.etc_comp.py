import streamlit as st

# age = st.slider("How old are you?", 시작, 끝, 초기값)
age = st.slider("How old are you?", 0, 100, 30)
st.write("I'm ", age, "years old")