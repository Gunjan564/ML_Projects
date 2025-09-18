import pickle
import pandas as pd
import os

class GroundwaterModel:
    def __init__(self):
        self.models = {}
        self.load_models()
    
    def load_models(self):
        """
        Load pre-trained pipelines (including preprocessing) for each month
        """
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            models_dir = os.path.join(base_dir, 'models')
            
            self.models['august'] = pickle.load(open(os.path.join(models_dir, 'model_august.pkl'), 'rb'))
            self.models['november'] = pickle.load(open(os.path.join(models_dir, 'model_november.pkl'), 'rb'))
            self.models['january'] = pickle.load(open(os.path.join(models_dir, 'model_january.pkl'), 'rb'))
            
            print("All models loaded successfully!")
        except FileNotFoundError as e:
            print(f"Error loading models: {e}")
            raise
    
    def predict(self, input_data, month='january'):
        """
        Predict groundwater level for a given month using the respective pipeline.
        
        Parameters:
        - [['Aquifer_Type', 'Geological_Zone', 'Annual_Rainfall_mm', 'WaterLevel_Jun_bgl']]
        - input should look like this:
            input_aug = {
                'Aquifer_Type': 'Unconfined',        # categorical
                'Geological_Zone': 'Kandi_Belt',    # categorical
                'Annual_Rainfall_mm': 750,          # numeric
                'WaterLevel_Jun_bgl': 15.5          # numeric
            }
        - input_data: dict with keys as feature names used in training
        - month: 'august', 'november', 'january'
        
        Returns:
        - float: predicted groundwater level
        """
        if month not in self.models:
            raise ValueError(f"Model for {month} not found. Available: {list(self.models.keys())}")
        
        # Convert dictionary to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Predict using the pipeline
        prediction = self.models[month].predict(input_df)
        
        return round(float(prediction[0]), 2)
        