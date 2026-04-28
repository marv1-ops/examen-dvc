import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Chargement des données
df = pd.read_csv('data/raw/raw.csv')

# Liste des colonnes numériques pertinentes selon l'énoncé
features = [
    'ave_flot_air_flow', 'ave_flot_level', 'iron_feed', 'starch_flow',
    'amina_flow', 'ore_pulp_flow', 'ore_pulp_pH', 'ore_pulp_density'
]
target = 'silica_concentrate'

# On ne garde que ce qui est utile (on exclut la colonne de date)
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

os.makedirs('data/processed', exist_ok=True)
X_train.to_csv('data/processed/X_train.csv', index=False)
X_test.to_csv('data/processed/X_test.csv', index=False)
y_train.to_csv('data/processed/y_train.csv', index=False)
y_test.to_csv('data/processed/y_test.csv', index=False)
