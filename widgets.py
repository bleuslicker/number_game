import streamlit as st
name = st.text_input('이름')
age = st.number_input('나이', min_value=1, max_value=120, value=20)
level = st.slider('난이도', 1, 10, 5)
menu = st.selectbox('메뉴', ['짜장', '짬뽕', '볶음밥'])
agree = st.checkbox('동의합니다')
if st.button('확인'):
    st.write(name, age, level, menu, agree)