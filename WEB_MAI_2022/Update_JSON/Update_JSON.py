import json


def change_json_file(name_file):
    with open(name_file, 'r') as file_json:
        data = json.load(file_json)
    file_json.close()
    data["quiz"]["maths"]["q3"] = {"question": "6 - 3", "options": ["0", "2", "3", "4"], "answer": "3"}
    with open(name_file, 'w') as file_json:
        file_json.write(json.dumps(data, indent=2))


def main():
    name = 'one.json'
    change_json_file(name)


if __name__ == "__main__":
    main()
