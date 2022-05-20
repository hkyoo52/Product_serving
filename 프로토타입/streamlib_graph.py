import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


st.title('이중 그래프')

filename = 'C:/Users/hkyoo52/Desktop/원빌딩/21년 서울 합계 + 2022년 1분기.xlsx'
df = pd.read_excel(filename, engine='openpyxl')

df=df.rename(columns=df.iloc[0])
df_2021 = df.iloc[:,[i for i in range(6)]][1:len(df)-5].reset_index()
df_2022 = df.iloc[:,[0,7,8,9,10,11]][1:len(df)-5].reset_index()

def make_bar(df,to_know):
    if to_know=='거래면적': to_know='거래면적(㎡)'
    elif to_know=='평당면적': to_know='거래면적(3.3㎡)'
    elif to_know=='평당가격' : to_know='3.3㎡당 가격(단위 :억)'
  
    possible=list(df.columns)+['거래면적','평당면적','평당가격']

    try:
        assert to_know in possible
    except:
        print('입력값은 {} 중에 하나여야 합니다.'.format(possible))

    fig=plt.figure(figsize=(20,10))
    ax=fig.add_subplot(1,1,1)

    idx=np.arange(len(df_2021['구'].index))
    ax.bar(idx, df[to_know],color='royalblue', label=to_know)

    ax.set_xticks([x for x in range(len(df))])
    ax.set_xticklabels(df_2021['구'].values,fontsize= 12, rotation= 45)
    ax.set_xlabel("지역", fontsize= 12)
    ax.set_ylabel(to_know, fontsize= 12)
    
    st.pyplot(fig)

def make_double_bar(df1,df2, to_know):
    if to_know=='거래면적': to_know='거래면적(㎡)'
    elif to_know=='평당면적': to_know='거래면적(3.3㎡)'
    elif to_know=='평당가격' : to_know='3.3㎡당 가격(단위 :억)'
    
    possible=list(df1.columns)+['거래면적','평당면적','평당가격']

    try:
        assert to_know in possible
    except:
        print('입력값은 {} 중에 하나여야 합니다.'.format(possible))

    fig=plt.figure(figsize=(20,10))
    ax=fig.add_subplot(1,1,1)
    idx=np.arange(len(df_2021['구'].index))
    width=0.35
    ax.bar(idx-width/2, df_2021[to_know],color='royalblue',width=width, label='과거')
    ax.bar(idx+width/2, df_2022[to_know],color='tomato',width=width, label='현재')

    ax.set_xticks([x for x in range(len(df1))])
    ax.set_xticklabels(df_2021['구'].values,fontsize= 12, rotation= 45)
    ax.set_xlabel("지역", fontsize= 12)
    ax.set_ylabel(to_know, fontsize= 12)

    st.pyplot(fig)




if st.checkbox('Show 2021 graph'):
    make_bar(df_2021,'평당가격')

if st.checkbox('Show 2022 graph'):
    make_bar(df_2022,'평당가격')

if st.checkbox('Show double graph'):
    make_double_bar(df_2021,df_2022,'평당가격')

