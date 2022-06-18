from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from setup import init_app
from clientService import ClientService
from carService import CarService
from testDriveService import TestDriveService
from dealerService import DealerService
from flask_login import login_user, logout_user, login_required, current_user
import error

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
def get_cars():
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


@app.route('/api/cars/filter/firm')
def get_firm_filter_values():
    """
    :return: JSON: {
    'values':[
        {
            "id":1,
            "name":""
        }
    ]
    }
    """
    cs = CarService()
    return {
        'values': [item.to_dict() for item in cs.get_firm_filter()]
    }


@app.route('/api/cars/filter/gearbox')
def get_gearbox_filter_values():
    """
    :return: JSON: {
    'values':[
        {
            "id":1,
            "name":""
        }
    ]
    }
    """
    cs = CarService()
    return {
        'values': [item.to_dict() for item in cs.get_gearbox_filter()]
    }


@app.route('/api/cars/filter/equipment')
def get_equipment_filter_values():
    """
    :return: JSON: {
    'values':[
        {
            "id":1,
            "name":""
        }
    ]
    }
    """
    cs = CarService()
    return {
        'values': [item.to_dict() for item in cs.get_equipment_filter()]
    }


@app.route('/api/cars/filter/type')
def get_type_filter_values():
    """
    :return: JSON: {
    'values':[
        {
            "id":1,
            "name":""
        }
    ]
    }
    """
    cs = CarService()
    return {
        'values': [item.to_dict() for item in cs.get_car_type_filter()]
    }


@app.route('/api/cars/filter/engine')
def get_engine_filter_values():
    """
    :return: JSON: {
    'values':[
        {
            "id":1,
            "name":""
        }
    ]
    }
    """
    cs = CarService()
    return {
        'values': [item.to_dict() for item in cs.get_engine_type_filter()]
    }


@app.route('/api/test-drive/create', methods=["POST"])
@login_required
def create_test_drive():
    """
    takes json: {
    "car_id": <int: auto`s id to test drive>,
    "date": <int: test drive date in format od unix time (seconds)>,
    "dealer_center_id": <int: id of dealer center>
    }
    :return: 200 or 40X error
    """
    auto_id = request.json.get('car_id')
    date = request.json.get('date')
    dealer_center = request.json.get('dealer_center_id')

    if not (auto_id and date and dealer_center):
        abort(400, 'Not correct value')

    tds = TestDriveService()
    try:
        tds.create_test_drive(auto_id, date, current_user.id, dealer_center)
    except error.BookTestDriveIsImpossible as e:
        abort(400, e.description)

    return jsonify(success=True)


@app.route('/api/test-drive/history')
@login_required
def get_test_drives():
    """
    :return: JSON: {
    "history: [
        {
        'car': "",
        'date': <int: unix time in seconds truncated to date>
        }
    ]
    }
    """

    tds = TestDriveService()
    return {
        "history": [item.to_dict() for item in tds.get_test_drives_by_client(current_user.id)]
    }


@app.route('/api/test-drive/dealer-centers')
@login_required
def get_dealer_centers():
    """
    :return: JSON: {
    "data":[
        {
            "address": "м.Київ, вул.Хрещатик, 17",
            "id": 2,
            "name": "Elite cars showroom"
        }
    ]
    }
    """
    ds = DealerService()
    return {
        'data': [item.to_dict() for item in ds.get_dealer_centers()]
    }


@app.route('/api/cars/test-drive/<int:test_drive_id>')
@login_required
def get_car_by_test_drive(test_drive_id: int):
    """
    ::return JSON: {
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
    """

    cs = CarService()
    return cs.get_car_by_test_drive(test_drive_id).to_dict()


app.run()
