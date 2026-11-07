import os
import json
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://dummy:1234@cluster0.qqeazm5.mongodb.net/tutedude_db?retryWrites=true&w=majority")

# Initialize db globally
db = None
try:
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = mongo_client["tutedude_db"]
except Exception as e:
    print(f"MongoDB Connection Warning: {e}")

@app.route('/api', methods=['GET'])
def get_json_data():
    file_path = os.path.join(app.root_path, 'data.json')
    try:
        if not os.path.exists(file_path):
            return jsonify({"error": "Data file not found"}), 404
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    
    if not item_name or not item_description:
        return jsonify({"error": "Item Name and Item Description are required"}), 400
        
    if db is None:
        return jsonify({"error": "Database connection not established"}), 500

    # Clean collection reference without typos
    collection = db["todo_collection"]
    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return jsonify({"message": "To-Do item added successfully to MongoDB"}), 201

@app.route('/')
def index():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)