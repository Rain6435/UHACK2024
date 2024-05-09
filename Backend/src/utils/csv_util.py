import pandas as pd  # Importing the pandas library for data manipulation
import json  # Importing the json module for JSON handling


def get_voie_routier() -> pd.DataFrame:
    """
    Retrieves data related to roadways from a CSV file and returns it as a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing data related to roadways.
    """
    df = pd.read_csv("./src/dataset/VOIE_PUBLIQUE.csv")  # Read data from the CSV file
    return df


def get_voie_routier_by_id(id):
    """
    Retrieves roadway data by ID from the dataset.

    Parameters:
        id: The ID of the roadway to retrieve.

    Returns:
        dict: Roadway data corresponding to the provided ID, serialized as a JSON-formatted dictionary.
    """
    df = get_voie_routier()  # Get roadway data
    location = df[df["CODEID"] == int(id)]  # Filter data by ID
    return json.loads(location.to_json(orient="records"))  # Serialize data as JSON


def get_pothole_test_data():
    """
    Retrieves test data related to potholes from a JSON file.

    Returns:
        dict: Test data related to potholes, loaded from the JSON file.
    """
    with open("./src/dataset/pothole_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)  # Load data from the JSON file
    return data
