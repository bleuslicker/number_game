import random
import streamlit as st
from number_utils import load_best, save_best

def new_game():
    st.session_state.answer= random.randint(1, 100)
    st.session_state.tries= 0
    st.session_state.msg = '1~100 사이의수를맞혀보세요!'
    st.session_state.done= False
if 'answer'not in st.session_state:   # 처음접속했을때만
    new_game()

st.title('★숫자맞히기게임')
best = load_best('best.txt')
if  best == 0:
    st.write('아직최고기록이없습니다.')
else:
    st.write(f'🏆현재최고기록: {best}번')
guess = st.number_input('1~100 사이의수', min_value=1,
max_value=100, step=1)

if st.button('확인', disabled=st.session_state.done):
    st.session_state.tries+= 1
    answer = st.session_state.answer
    if guess < answer:
        st.session_state.msg = f'{guess} → UP! ⬆'
    elif guess > answer:
        st.session_state.msg = f'{guess} → DOWN! ⬇'
    else:
        tries = st.session_state.tries
        st.session_state.msg = f'정답! {tries}번만에맞혔습니다.'
        st.session_state.done= True
        if best == 0 or tries < best:
            save_best('best.txt', tries)
            st.session_state.msg += ' 🎉최고기록갱신!'
        st.rerun()


st.info(st.session_state.msg)
st.write(f'시도횟수: {st.session_state.tries}번')
if st.session_state.done:
    st.balloons()
    if st.button('새게임'):
        new_game()
        st.rerun()