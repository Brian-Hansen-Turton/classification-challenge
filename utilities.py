import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def createTrainingSets(data, y_column):
    # clean the data
    data = data.dropna
    # Create the X (features)      
    X = data.drop(columns=[y_column]) 
    # Create the y (prediction) 
    y = data[y_column].copy()   
    # return the features and the predictions
    return X, y
