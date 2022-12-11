import requests
r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, r.text, r.json())
r = requests.post('http://127.0.0.1:5000/users', json={"id": 3, "name": "Peter", "surname": "Ibrov"})
print(r.json())
r = requests.delete('http://127.0.0.1:5000/users', json={"id": 1})
print(r.json())
r = requests.put('http://127.0.0.1:5000/users', json={"id": 3, "name": "Albert", "surname": "Einstein"})
print(r.json())
