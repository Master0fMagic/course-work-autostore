from flask_login import UserMixin


class Client(UserMixin):
    def __init__(self, client_id=-1, login="", password=""):
        self._password = password
        self._login = login
        self._id = client_id

    @property
    def id(self) -> int:
        return self._id

    @property
    def password(self) -> str:
        return self._password

    @property
    def login(self) -> str:
        return self._login


class Car:
    def __init__(self, car_id=-1, year=-1, equipment='', engine='', gearbox='', engine_volume=None,
                 car_type='', firm='', model='', horse_powers=-1, battery=None):
        self._id = car_id
        self._year = year
        self._equipment = equipment
        self._engine = engine
        self._gearbox = gearbox
        self._engine_volume = engine_volume
        self._car_type = car_type
        self._firm = firm
        self._model = model
        self._horse_powers = horse_powers
        self._battery = battery

    @property
    def id(self) -> int:
        return self._id

    @property
    def produce_year(self) -> int:
        return self._year

    @property
    def equipment(self) -> str:
        return self.equipment

    @property
    def engine(self) -> str:
        return self._engine

    @property
    def engine_volume(self) -> float:
        return self._engine_volume

    @property
    def car_type(self) -> str:
        return self._car_type

    @property
    def firm(self) -> str:
        return self._firm

    @property
    def model(self) -> str:
        return self._model

    @property
    def horse_powers(self) -> int:
        return self._horse_powers

    @property
    def battery_capacity(self) -> float:
        return self._battery

    def to_dict(self) -> dict:
        return {
            'id': self._id,
            'produce_year': self._year,
            'equipment': self._equipment,
            'engine': self._engine,
            'car_type': self._car_type,
            'firm': self._firm,
            'model': self._model,
            'horse_powers': self._horse_powers,
            'engine_volume': self._engine_volume,
            'battery_capacity': self._battery
        }


class TestDrive:
    def __init__(self, car='', time=0):
        self._car = car
        self._date = time

    @property
    def car(self) -> str:
        return self._car

    @property
    def time(self) -> int:
        return self._date

    def to_dict(self) -> dict:
        return {
            'car': self._car,
            'date': self._date
        }


class FilterItem:
    def __init__(self, id=-1, name=''):
        self._id = id
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name
        }


class DealerCenter:
    def __init__(self, center_id=0, name='', address=''):
        self._id = center_id
        self._name = name
        self._address = address

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def address(self) -> str:
        return self._address

    def to_dict(self) -> dict:
        return {
            'id': self._id,
            'name': self._name,
            'address': self.address
        }
