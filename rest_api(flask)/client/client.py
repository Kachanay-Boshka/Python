import requests
r = requests.get('http://127.0.0.1:5000/owners')
# r = requests.post('http://127.0.0.1:5000/owners', json={"name": "Heather", "surname": "Anderson", "phone number": "8(955)12432786"})

# id_owner_del = 770508
# r = requests.delete(f'http://127.0.0.1:5000/owners/{id_owner_del}')

# id_owner_put = 1
# r = requests.put(f'http://127.0.0.1:5000/owners/{id_owner_put}', json={"name": "Kirill", "surname": "Anderson", "phone_number": "8(955)12432786"})

# id_owner_get = 1
# r = requests.get(f'http://127.0.0.1:5000/owners/{id_owner_get}')
# r = requests.get(f'http://127.0.0.1:5000/owners/{id_owner_get}/cars')
# r = requests.post(f'http://127.0.0.1:5000/owners/{id_owner_get}/cars', json={"body_type": "Cabriolet", "color": "Black", "model": "Kia"})

# id_owner = 1
# id_car = 576305
# r = requests.delete(f'http://127.0.0.1:5000/owners/{id_owner}/cars/{id_car}')

# id_owner = 1
# id_car = 1
# r = requests.put(f'http://127.0.0.1:5000/owners/{id_owner}/cars/{id_car}', json={"color": "Yellow"})