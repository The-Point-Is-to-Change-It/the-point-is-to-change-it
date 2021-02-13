from api.v1 import api_v1
from flask import jsonify, request

@api_v1.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    from models.user import User
    form = request.form
    name, email = form.get('name'), form.get('email')
    handle, password = form.get('handle'), form.get('password')
    user_data = {
        'name': name,
        'email': email,
        'handle': handle,
        'password': password
    }
    new_user = User(**user_data)
    response = {
        'status': 'OK',
        'user': new_user.to_dict()
    }
    return jsonify(response), 200