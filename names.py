import streamlit as st

if 'names' not in st.session_state:
    st.session_state.names = []

name = st.text_input('이름')
if st.button('추가') and name != '':
    st.session_state.names.append(name)
st.write('지금까지', len(st.session_state.names), '명')
for n in st.session_state.names:
    st.write('-', n)
if st.button('모두지우기'):
    st.session_state.names = []
st.rerun()



