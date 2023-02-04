# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON_sk = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user_sk = json.loads(userJSON_sk)

print(user_sk)
print(user_sk['first_name'])

car_sk = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_sk = json.dumps(car_sk)

print(carJSON_sk)