from flask import Flask, request, jsonify
from flask_cors import CORS
import json

api = Flask(__name__)
CORS(api, origins=['http://localhost:5173'])

@api.route('/CPUUseageData')
def CPUUseageData():
    file_path = "CPUUseageData.json"
    response_body = read_json_file(file_path)
    return response_body

@api.route('/Performance')
def Performance():
    file_path = "Performance.json"
    response_body = read_json_file(file_path)
    return response_body

@api.route('/RealTimeStatus')
def RealTimeStatus():
    file_path = "RealTimeStatus.json"
    response_body = read_json_file(file_path)
    return response_body

@api.route('/chip', methods=['POST'])
def receive_data():
    data = request.get_json()
    received_data = data['data']
    
    print(received_data)
    
    response_data = {'message': 'Data received successfully'}
    return jsonify(response_data)


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


if __name__ == '__main__':
    api.run()
