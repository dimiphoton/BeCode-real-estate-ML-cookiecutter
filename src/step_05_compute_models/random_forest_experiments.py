from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

def experiment_1(df):
    y=df[[('Target','logPrice')]]
    X=df[['Group 1','my features']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)


    # Create a linear regression model
    model = RandomForestRegressor(n_estimators=100)

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = model.predict(X_test)

    # print feature importance
    print(model.feature_importances_)
    
    # Calculate the R^2 score for the model
    score = model.score(X_test, y_test)
    print("R^2 score: ", score)
    return model
