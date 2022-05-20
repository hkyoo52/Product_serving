import streamlit as st
import pandas as pd
import numpy as np

# 제목 만들기
st.title("Title")

# 바로 아래 글쓰기
st.write("Write Something")

# 버튼 만들기
if st.button("click button"):
    st.write("Data Loading..")

# 체크박스 만들기 (이름 : Checktbox Button)
# 버튼 클릭하면 글씨를 써라
checkbox_btn = st.checkbox('Checktbox Button')
if checkbox_btn:
    st.write('Great!')
# 체크박스 만드는데 기본으로 체크하게 만듬
checkbox_btn2 = st.checkbox('Checktbox Button2', value=True)
if checkbox_btn2:
    st.write('Button2')

# Radio 버튼 만들기
selected_item = st.radio("Radio Part", ("A", "B", "C"))
# A가 누르면 A!!를 써라
if selected_item == "A":
    st.write("A!!")
elif selected_item == "B":
    st.write("B!")
elif selected_item == "C":
    st.write("C!")

# 선택박스 만들기 -> 선택 가능 박스 : kyle, seongyun, zzsza
option = st.selectbox('Please select in selectbox!',
                    ('kyle', 'seongyun', 'zzsza'))
# 선택한 박스 글쓰기
st.write('You selected:', option)

# 여러개 선택 가능 박스 만들기
multi_select = st.multiselect('Please select somethings in multi selectbox!',
                            ['A', 'B', 'C', 'D'])

st.write('You selected:', multi_select)

# 슬라이더 만들기
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)