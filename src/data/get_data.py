import pandas as pd
import os

def get_data():
    url = "https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv"
    save_path = "data/raw/raw.csv"
    
    # Création du dossier s'il n'existe pas
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Téléchargement et sauvegarde
    df = pd.read_csv(url)
    df.to_csv(save_path, index=False)
    print(f"Données téléchargées et sauvegardées dans {save_path}")

if __name__ == "__main__":
    get_data()
