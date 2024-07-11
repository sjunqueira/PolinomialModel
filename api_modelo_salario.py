from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Instanciar FastAPI
app = FastAPI()

#Criar classe com dados de entrada
class request_body(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int

#Carregar modelo para realizar a predição
model_poly = joblib.load('./modelo_salario.pkl')

@app.post('/predict')
def predic(data: request_body):

    input_features = {
    'tempo_na_empresa': data.tempo_na_empresa,
    'nivel_na_empresa': data.nivel_na_empresa
    }

    df_pred = pd.DataFrame(input_features, index=[1])

    y_pred = model_poly.predict(df_pred)[0].astype(float)

    return {'salario_em_reais': y_pred.tolist()}