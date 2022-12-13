import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("서울시의 모기 파악하기")
st.header("모기예보제와 일자별 날씨 데이터를 통한)
st.header("모기 발생 빈도 변화 파악")

st.image("https://news.seoul.go.kr/welfare/files/2020/02/62cfc9f3f36041.41905113-1086x1536.jpg")
st.write("http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#", fontcolor = '#CECECE')

# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df1 = pd.read_csv('./Mini_project_1/mosdata.csv', encoding='cp949')
df2 = df1[:2517]
df2

#lp_1 = sns.lineplot(data=df2, x='모기지수 발생일',y='모기지수(수변부)')
#lp_2 = sns.lineplot(data=df2, x='모기지수 발생일',y='모기지수(주거지)')
#lp_3 = sns.lineplot(data=df2, x='모기지수 발생일',y='모기지수(공원)')
#plt.show(lp_1,lp_2,lp_3)