from model import Prediction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediction: 
    if len(inputs) != len(outputs):
        raise ValueError("Inputs and outputs must have the same length.")
    
    # Create DataFrame for data
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})
    
    # Reshape the data NumPy (X: inputs, y: outputs)
    X = np.array(df['inputs']).reshape(-1, 1)
    y = np.array(df['outputs']).reshape(-1, 1)
    
    # Split the data into training and testing sets
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Initialize the model and test it 
    model = LinearRegression()
    model.fit(train_X, train_y)
    
    # Predictions
    y_predict = model.predict([[input_value]])
    y_line = model.predict(X)
        
    return pass