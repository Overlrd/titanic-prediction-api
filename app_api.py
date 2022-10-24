from fastapi import FastAPI
import keras
import pandas as pd
from pydantic import BaseModel



# load the model
model_path ='titanic_model.h5'
model = keras.models.load_model(model_path)



class fit_item(BaseModel):
    Pclass : int
    Sex    : int
    Sibsp  : int
    Parch   : int
    Embarked  : int
    CabinBool : int
    AgeGroup : float
    Title: int
    Fareband : int




app = FastAPI()

@app.post('/')
async def response(item : fit_item):
    #result = pd.DataFrame(data={"test_data":df['Embarked'], "pred":pred}).astype(int)
    #result = result.to_numpy()
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    pred = model.predict(df).flatten()
    return {'result':int(pred)}