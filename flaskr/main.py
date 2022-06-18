from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from setup import init_app
from clientService import ClientService
from carService import CarService
from flask_login import login_user, logout_user, login_required, current_user
import error
import dto

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*", "supports_credentials": "true"}})
init_app(app)


@app.route('/api/login', methods=['POST'])
def login():
    """
    takes json: {
    "login":"user_email_or_phone_number",
    "password":"user_password"
    }

    creates user session
    :return: success or error
    """
    userdata = request.json['login']
    password = request.json['password']

    if not (userdata and password):
        abort(400, 'required field empty')

    cs = ClientService()
    try:
        user = cs.login(userdata, password)
        login_user(user)
    except (error.UseNotFoundException, error.WrongPasswordException) as er:
        abort(401, er.description)

    return jsonify(success=True)


@app.route('/api/logout')
@login_required
def logout():
    """
       ends user session
       :return: 200 ok
    """
    logout_user()
    return jsonify(success=True)


@app.route('/api/sing-up', methods=['POST'])
def sing_up():
    """
       takes json: {
       "email":"",  //field does not required
       "password":"",
       "repeated_password":"",
       "first_name":"",
       "last_name":"",
       "phone":"",
       }

       create new user and login him
       :return: success or error
       """

    user_login = request.json.get('login')
    password = request.json.get('password')
    repeated_password = request.json.get('repeated_password')

    if not (password and repeated_password and user_login):
        abort(400, 'missing required fields')

    if password != repeated_password:
        abort(400, 'passwords does not match')

    cs = ClientService()
    client = cs.register_new_user(user_login, password)
    login_user(client)
    return jsonify(success=True)


@app.route('/api/cars')
def ge_cars():
    """
    :return JSON: {
        cars: [
         {
            'id': 1,
            'produce_year': 2000,
            'equipment': "",
            'engine': "",
            'car_type': "",
            'firm': "",
            'model': "",
            'horse_powers': 1,
            'battery_capacity': 0.0 // or null if not set
            'engine_volume': 0.0 //or null if not set
        }
        ]
    }
    """
    cs = CarService()
    return {
        'cars': [car.to_dict() for car in cs.get_cars()]
    }

# app.run()
