import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")

# 데이터프레임 만들기
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# 차트 만들기
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# 지도에 점 그리기
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)


# 체크박스가 클릭하면 데이터프레임을 띄워라
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data


# Add a placeholder 진행상황을 알려준다
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')    # bar 위에 글씨를 써준다.
  bar.progress(i + 1)                          # bar 진행상황을 알려준다
  time.sleep(0.1)


