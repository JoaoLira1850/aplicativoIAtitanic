from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware

model = joblib.load("titanic_model.pkl")



FEATURES = [
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Pclass_2",
    "Pclass_3",
    "Embarked_Q",
    "Embarked_S",
]

app = FastAPI()


origins = [
    "http://localhost:8081",
    "http://127.0.0.1:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

class Passager(BaseModel):
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Pclass_2: int
    Pclass_3: int
    Embarked_Q: int
    Embarked_S: int

@app.get("/")

def root():
    return {"message": "Api esta rodando !!"}


@app.post("/predict")
def predit(passager: Passager):

    try:

        data = pd.DataFrame([passager.model_dump()])[FEATURES]

        pred = model.predict(data)[0]

        prob = model.predict_proba(data)[0][1]

        return{
            "sobreviveu": int( pred),
            "Probabilidade" :float(prob),
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code = 500, detail = str(e))
