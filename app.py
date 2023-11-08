from flask import Flask, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("mongodb", 27017)
db = client.mydb
collection = db.mycollection


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    result = collection.insert_one({'key': key, 'value': value})
    return jsonify({'_id': str(result.inserted_id)})


@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    key = data.get('key')
    new_value = data.get('new_value')
    result = collection.update_one({'key': key},
                                   {'$set': {'value': new_value}})
    return jsonify({'modified_count': result.modified_count})


@app.route('/read', methods=['GET'])
def read():
    key = request.args.get('key')
    result = collection.find_one({'key': key})
    if result:
        return jsonify({'key': result['key'], 'value': result['value']})
    return jsonify({'message': 'Key not found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
