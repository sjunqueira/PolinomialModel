import streamlit as st
import json
import requests

#Criar título da aplicação
st.title('Modelo de predição de salario')

#Inputs do modelo
st.write('Há quantos meses o profissional está na empresa?')
tempo_na_empresa = st.slider('Meses',min_value=0, max_value=180, value=60, step=1)

st.write('Qual o nível do profissional na empresa?')
nivel_na_empresa = st.slider('Nivel',min_value=0, max_value=10, value=5, step=1)

#Preparar dados para API
input_features = {'tempo_na_empresa': tempo_na_empresa,
                  'nivel_na_empresa': nivel_na_empresa}

#Criar um botão e capturar o evento
if st.button('Estimar salário'):
    res = requests.post(url = 'http://127.0.0.1:8000/predict', data=json.dumps(input_features))

    res_json = json.loads(res.text)
    salario_em_reais = round(res_json['salario_em_reais'], 2)
    st.subheader(f'O salário estimado é de: {salario_em_reais}')