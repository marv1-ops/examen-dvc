import pandas as pd
import json
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

X_test = pd.read_csv('data/processed/X_test_scaled.csv')
y_test = pd.read_csv('data/processed/y_test.csv').values.ravel()
model = joblib.load('models/model.pkl')

predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Sauvegarde des scores
os.makedirs('metrics', exist_ok=True)
with open('metrics/scores.json', 'w') as f:
    json.dump({'mse': mse, 'r2': r2}, f)

# Sauvegarde des prédictions
pd.DataFrame(predictions, columns=['predictions']).to_csv('data/predictions.csv', index=False)
