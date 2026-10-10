# NOTAS DE ESTUDOS 


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd





dados =  pd.read_excel('vendas.xlsx')
print(dados)


df =  pd.DataFrame(dados)


X = df[['Meses']] # bidimensional (colchetes duplos)
y = df['Vendas']


modelo =  LinearRegression()


modelo.fit(X,y)


novo = pd.DataFrame({'Meses':[9]})


resultado = modelo.predict(novo)


print(resultado[0])