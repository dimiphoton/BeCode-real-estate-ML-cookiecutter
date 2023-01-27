import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, max_error
from sklearn.model_selection import train_test_split

def experiment_1(df):
    y=df.loc['sale'][('Target','logPrice')]
    X=df.loc['sale'][['Group 1','my features']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    # Convert data to DMatrix for use with XGBoost
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    # Define the parameters for the XGBoost model
    params = {
        'objective': 'reg:linear',
        'max_depth': 3,
        'eta': 0.1,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'eval_metric': 'mae'
    }

    # Train the XGBoost model
    model = xgb.train(params, dtrain, num_boost_round=1000)


    # Make predictions on the test set
    y_pred = model.predict(dtest)

    # Calculate the mean absolute error
    mae = mean_absolute_error(y_test, y_pred)
    print('Mean Absolute Error:', mae)
    return model