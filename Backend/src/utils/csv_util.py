import pandas as pd
import json


def get_voie_routier() -> pd.DataFrame:
    df = pd.read_csv('./src/dataset/VOIE_PUBLIQUE.csv')
    return df