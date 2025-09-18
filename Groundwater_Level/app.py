from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import pickle
import pandas as pd
import os

class GroundwaterInput(BaseModel):
    Aquifer_Type: str
    Geological_Zone: str
    Annual_Rainfall_mm: float
    WaterLevel_Jun_bgl: float = None   # Only for August
    WaterLevel_Aug_bgl: float = None   # Only for November
    WaterLevel_Nov_bgl: float = None   # Only for January
    month: Literal['august', 'november', 'january']
class GroundwaterModelAPI:
    def __init__(self):
        self.models = {}
        base_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(base_dir, 'models')
        self.models['august'] = pickle.load(open(os.path.join(models_dir,r'C:\Users\hp\OneDrive\Desktop\ML_Projects\Groundwater_Level\model_august.pkl'), 'rb'))
        self.models['november'] = pickle.load(open(os.path.join(models_dir,r'C:\Users\hp\OneDrive\Desktop\ML_Projects\Groundwater_Level\model_november.pkl'), 'rb'))
        self.models['january'] = pickle.load(open(os.path.join(models_dir,r'C:\Users\hp\OneDrive\Desktop\ML_Projects\Groundwater_Level\model_january.pkl'), 'rb'))
        
    def predict(self, data: dict, month: str):
        input_df = pd.DataFrame([data])
        pred = self.models[month].predict(input_df)
        return round(float(pred[0]), 2)
    
# Initialize
groundwater_model = GroundwaterModelAPI()
app = FastAPI()
@app.get("/")
def root():
    return {"message": "Groundwater API is running!"}
@app.post("/predict/")
def predict_water_level(input_data: GroundwaterInput):
    data = input_data.dict()
    month = data.pop('month')
    
    # Remove irrelevant columns for each month
    if month == 'august':
        data.pop('WaterLevel_Aug_bgl', None)
        data.pop('WaterLevel_Nov_bgl', None)
    elif month == 'november':
        data.pop('WaterLevel_Jun_bgl', None)
        data.pop('WaterLevel_Nov_bgl', None)
    elif month == 'january':
        data.pop('WaterLevel_Jun_bgl', None)
        data.pop('WaterLevel_Aug_bgl', None)
    
    prediction = groundwater_model.predict(data, month)
    return {"month": month, "predicted_water_level": prediction}