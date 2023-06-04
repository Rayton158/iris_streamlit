import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)

df['target'] = iris.target

df.loc[df['target']==0,'target'] = 'setosa'
df.loc[df['target']==1,'target'] = 'versicolor'
df.loc[df['target']==2,'target'] = 'virginica'

x = iris.data[:,[0,2]]
y = iris.target

clf = LogisticRegression()
clf.fit(x,y)

st.sidebar.header('input features')

sepalvalue = st.sidebar.slider('sepal length (cm)',min_value=0.0,max_value=10.0,step=0.1)
petalvalue = st.sidebar.slider('petalvalue (cm)',min_value=0.0,max_value=10.0,step=0.1)

st.title('Iris Classifier')
st.write('### Input Value')

value_df = pd.DataFrame([],columns=['data','sepal length (cm)','petal length (cm)'])
record =pd.Series(['data',sepalvalue,petalvalue],index=value_df.columns)
value_df = pd.concat([value_df,pd.DataFrame([record])],ignore_index=True)
value_df.set_index('data',inplace=True)

st.write(value_df)

pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs,columns = ['setosa','versicolor','virginica'],index=['probability'])

st.write('##Prediction')
st.write(pred_df)

name = pred_df.idxmax(axis=1).tolist()
st.write('##Result')
st.write('このアイリスはきっと',str(name[0]),'です！')