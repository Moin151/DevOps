import os
import json
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection Setup
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://user:pass@cluster.mongodb.net/test?retryWrites=true&w=majority")
try:
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = mongo_client["tutedude_db"]
    collection = db["todo_collection"]
except Exception as e:
    print(f"MongoDB Connection Warning: {e}")

# Task 1 & 2: JSON API Route
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

# Task 3: Backend route for To-Do item submission
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    
    if not item_name or not item_description:
        return jsonify({"error": "Item Name and Item Description are required"}), 400
        
    db.todo_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return jsonify({"message": "To-Do item added successfully to MongoDB"}), 201

@app.route('/')
def index():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)