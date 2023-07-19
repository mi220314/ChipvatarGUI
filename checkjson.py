import json

def read_json_file(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error while decoding JSON file '{file_path}'. Invalid JSON format.")
    
    return None

def print_json_data(json_data):
    if json_data:
        print("JSON data:")
        print(json.dumps(json_data, indent=4))
    else:
        print("No valid JSON data to print.")

# Provide the file path of your JSON file
file_path = "test.json"

json_data = read_json_file(file_path)
print_json_data(json_data)