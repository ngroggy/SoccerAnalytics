import pandas as pd
import json
import zipfile
from pathlib import Path

def dataloader(matchid, input_basepath='./input/wyscout/', output_basepath='./results/wyscout/'):
    """Return the data of one game from the Wyscout dataset and save it as a csv file."""

    # If the csv file already exists, load it
    if Path(f"{output_basepath}{matchid}_df_events.csv").exists():
        return pd.read_csv(f"{output_basepath}{matchid}_df_events.csv")
    
    # Create the directory for unzipped data if it does not exist
    unzip_dir = f"{input_basepath}{matchid}/"

    if not Path(unzip_dir).exists():
        Path(unzip_dir).mkdir(parents=True, exist_ok=True)

    # Else unzip the data and save it as a csv file
    zip_folder = unzip_dir[:-1] + '.zip'

    # Extract the zip file
    with zipfile.ZipFile(zip_folder, 'r') as zip_ref:
        zip_ref.extractall(Path(unzip_dir))

    # Load the json file
    with open(f"{unzip_dir}{matchid}.json", encoding='utf8') as f:
        js = json.load(f)
        df_events = pd.json_normalize(js['events'])

    # Save the data as a csv file
    if not Path(output_basepath).exists():
        Path(output_basepath).mkdir(parents=True, exist_ok=True)

    df_events.to_csv(f"{output_basepath}{matchid}_df_events.csv")

    return df_events
