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
