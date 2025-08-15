from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import numpy as np

app = FastAPI(title="ML model API")

X = np.array([[i] for i in range(10)])
y = np.array([i % 2 for i in range(10)])

model = LogisticRegression()
model.fit(X, y)

class NumberInput(BaseModel):
    number: int

@app.post("/predict")
def predict(input_data: NumberInput):
    try:
        num = np.array([[input_data.number]])
        prediction = model.predict(num)[0]
        label = "Even" if prediction == 0 else "Odd"
        
        return {
            "number": input_data.number, 
            "prediction": label,
            "prediction_value": int(prediction)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_trained": True}