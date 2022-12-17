from flask import Flask, request, render_template, jsonify, redirect
import json
import psycopg2
import random
app = Flask(__name__)
conn = psycopg2.connect(
    host="localhost",
    database="car",
    user="postgres",
    password="1478520",
    port=5434
)
cursor = conn.cursor()
success_message = {'success': True}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/owners', methods=['GET'])
def get_owners():
    data_owners = []
    sql = 'SELECT * FROM owner'
    cursor.execute(sql)
    data = cursor.fetchall()
    for single_owner in data:
        data_owners.append({'id': single_owner[0],
                            'name': single_owner[1],
                            'surname': single_owner[2],
                            'phone number': single_owner[3]})
    print(data_owners)
    print(request.url)
    return render_template('owners.html', owners=data_owners)


@app.route('/owners/<id_owner>', methods=['GET'])
def get_owner(id_owner):
    data_owners = []
    sql = 'SELECT * FROM owner WHERE id_owner = %s'
    cursor.execute(sql, (id_owner,))
    data = cursor.fetchall()
    for single_owner in data:
        data_owners.append({'id': single_owner[0],
                            'name': single_owner[1],
                            'surname': single_owner[2],
                            'phone number': single_owner[3]})
    print(data_owners)
    print(request.url)
    return render_template('owner.html', owners=data_owners[0])


@app.route('/owners', methods=['POST'])
def add_owner():
    sql = 'INSERT INTO owner VALUES (%s, %s, %s, %s)'
    id = random.randint(1, 999999)
    name = request.get_json()['name']
    surname = request.get_json()['surname']
    ph_number = request.get_json()['phone number']
    cursor.execute(sql, (id, name, surname, ph_number))
    conn.commit()
    return get_owner(id)


@app.route('/owners/<id_owner>', methods=['DELETE'])
def del_owners(id_owner):
    sql = 'DELETE FROM owner WHERE id_owner = %s'
    cursor.execute(sql, (id_owner,))
    conn.commit()
    return get_owners()


@app.route('/owners/<id_owner>', methods=['PUT'])
def update_owner(id_owner):
    sql = 'UPDATE owner SET name = %s, surname = %s, phone_number = %s WHERE id_owner = %s'
    name = request.get_json()['name']
    surname = request.get_json()['surname']
    phone_number = request.get_json()['phone_number']
    cursor.execute(sql, (name, surname, phone_number, id_owner))
    conn.commit()
    return get_owner(id_owner)


@app.route('/owners/<id_owner>/cars', methods=['GET'])
def get_cars(id_owner):
    sql = 'SELECT * FROM car, owner WHERE owner.id_owner = car.id_owner and car.id_owner = %s'
    cursor.execute(sql, (id_owner,))
    data = cursor.fetchall()
    car_data = []
    if not not data:
        for car in data:
            car_data.append({'id_car': car[0],
                             'color': car[1],
                             'body_type': car[4],
                             'brand': car[3],
                             'id_owner': car[5],
                             'name': car[6],
                             'surname': car[7],
                             'phone_number': car[8]})
        print(car_data)
        print(request.url)
    return render_template('cars.html', data=car_data, id=id_owner)


@app.route('/owners/<id_owner>/cars/<id_car>', methods=['GET'])
def get_car(id_owner, id_car):
    sql = 'SELECT * FROM car WHERE (id_owner = %s) AND (id_car = %s)'
    cursor.execute(sql, (id_owner, id_car))
    data = cursor.fetchall()
    car_data = []
    if not not data:
        for car in data:
            car_data.append({'id_car': car[0],
                             'color': car[1],
                             'body_type': car[4],
                             'brand': car[3]})
        print(car_data)
        print(request.url)
    return render_template('car.html', data=car_data[0], id=id_owner)


@app.route('/owners/<id_owner>/cars', methods=['POST'])
def add_car(id_owner):
    sql = 'INSERT INTO car' \
          '(id_car, id_owner, body_type, color, model) ' \
          'VALUES (%s, %s, %s, %s, %s)'
    id = random.randint(1, 999999)
    body_type = request.get_json()['body_type']
    color = request.get_json()['color']
    model = request.get_json()['model']
    cursor.execute(sql, (id, id_owner, body_type, color, model))
    conn.commit()
    return get_cars(id_owner)


@app.route('/owners/<id_owner>/cars/<id_car>', methods=['DELETE'])
def del_car(id_owner, id_car):
    sql = 'DELETE FROM car WHERE (id_owner = %s) AND (id_car = %s)'
    cursor.execute(sql, (id_owner, id_car))
    conn.commit()
    return get_cars(id_owner)


@app.route('/owners/<id_owner>/cars/<id_car>', methods=['PUT'])
def update_car(id_owner, id_car):
    sql = 'UPDATE car SET color = %s WHERE (id_owner = %s) AND (id_car = %s)'
    color = request.get_json()['color']
    cursor.execute(sql, (color, id_owner, id_car))
    conn.commit()
    return get_cars(id_owner)


if __name__ == '__main__':
    app.run(debug=True)

