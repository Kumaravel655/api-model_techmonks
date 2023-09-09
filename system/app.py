from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load JSON data from a file
with open('kumaravel.json', 'r') as file:
    sample_data = json.load(file)

@app.route('/getTimeStories', methods=['GET'])
def get_json_data():
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
