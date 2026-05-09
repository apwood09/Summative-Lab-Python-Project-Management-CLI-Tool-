import json
import os 

DATA_PATH = "data/"

def save_data(filename, data_list):
    """Saves a list of objects to a JSON file."""
    
    target_path = filename if os.path.isabs(filename) else os.path.join(DATA_PATH, filename)
    

    directory = os.path.dirname(target_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(target_path, "w") as f:
        json.dump([obj.__dict__ for obj in data_list], f, indent=4)

def load_data(filename, cls):
    """Loads JSON data and maps back to class instances."""
    target_path = filename if os.path.isabs(filename) else os.path.join(DATA_PATH, filename)
    
    try:
        with open(target_path, "r") as f:
            raw_data = json.load(f)
            return [cls(**item) for item in raw_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []