import json
from flask import Flask, jsonify, request
app = Flask(__name__)
data = [{'id': 0, 'name': 'Alex', 'surname': 'Turner'},
        {'id': 1, 'name': 'Thom', 'surname': 'Yorke'}]


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)


@app.route('/users', methods=['POST'])
def add_user():
    data.append(request.get_json())
    return jsonify(data)


@app.route('/users', methods=['DELETE'])
def del_user():
    for data_dic in data:
        if data_dic['id'] == request.get_json()['id']:
            data.remove(data_dic)
    return jsonify(data)


@app.route('/users', methods=['PUT'])
def update_user():
    for data_dic in data:
        if data_dic['id'] == request.get_json()['id']:
            data_dic['name'] = request.get_json()['name']
            # data_dic['surname'] = request.get_json()['surname']
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
