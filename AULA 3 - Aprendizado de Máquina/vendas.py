# NOTAS DE ESTUDOS 




import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header('Previsão de Vendas')

#Dados: [Investimento em Marketing] -> faturamento
dados_vendas = pd.DataFrame({
'investimento': [100, 200, 300, 400, 500, 600],
'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

#Objetivo: previsão de FATURAMENTO baseado nos INVESTIMENTOS

#st.scatter_chart(previsão, x = 'investimento', y= 'faturamento')
modelo_previsao = LinearRegression() 
modelo_previsao.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])


v_investido = st.number_input('Valor investido?')
f_final = modelo_previsao.predict([[v_investido]])
print(f_final)


if f_final > 5100:
    st.write('Faturamento superado')
elif f_final >= 3200 and f_final < 4800:
    st.write('Faturamento padrão')
else:
    st.write('Faturamento abaixo do esperado')    



#v_investido = st.slider('horas de estudos', 0,12,5)
#nota_final = modelo_escola.predict([[h_estudo]])
#print(nota_final)

#st.metric(f'sua nota seria' ,f'{min(nota_final[0], 10.0):.1f}')

