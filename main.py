from fastapi import FastAPI
import joblib

# Initialize FastAPI
app = FastAPI()

# Load the regression model
model = joblib.load("regression.joblib")

@app.post("/predict")
async def predict(size: float, bedrooms: int, garden: int):
    input_data = [[size, bedrooms, garden]]
    prediction = model.predict(input_data)
    return {"predicted_price": prediction[0]}