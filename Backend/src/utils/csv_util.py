import pandas as pd
import json


def get_voie_routier() -> pd.DataFrame:
    df = pd.read_csv('./src/dataset/VOIE_PUBLIQUE.csv')
    return df

def get_voie_routier_by_id(id):
    df = get_voie_routier()
    location = df[df['CODEID'] == int(id)]
    return json.loads(location.to_json(orient='records'))