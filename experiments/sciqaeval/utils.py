import json
import os

def read_json(file_path):
    """Reads a JSON file and returns the data as a Python dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return None

def save_json(data, file_path, indent=4):
    """Saves a Python dictionary as a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=indent)
    except Exception as e:
        print(f"Error saving JSON file: {e}")

def mkdir(path):
    """Creates a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)