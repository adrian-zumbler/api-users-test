from flask import Flask, json, request

app = Flask(__name__)

test_data = [
    {'id': 1, 'name': "Adrian"},
    {'id': 2, 'name': "Bob"},
    {'id': 3, 'name': "John"}
]

# Get All Users
@app.route('/users',methods=['GET'])
def get_users():
    return json.dumps(test_data)

# Get User By Id
@app.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
    return json.dumps(select_user(user_id))

# Create Users
@app.route('/users', methods=['POST'])
def create_user():
    test_data.append(request.json)
    return json.dumps(test_data)

# Update User by Id
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = select_user(user_id)
    return 'Hello, World!'


# Delete User by Id
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user():
    return 'Hello, World!'


def select_user(self,user_id):
    return user for user in test_data if user['id'] == user_id