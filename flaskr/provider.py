from abc import ABC, abstractmethod
import dto
import sqlite3
import converter


class SqliteDatabaseProvider:
    def execute_select(self, query: str):
        connection = sqlite3.connect('./autostore.db')
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return records

    def execute_update(self, query):
        connection = sqlite3.connect('./autostore.db')
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return res


class AbstractClientProvider(ABC):
    @abstractmethod
    def is_login_exist(self, login: str) -> bool:
        pass

    @abstractmethod
    def check_password(self, login: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_client(self, login: str) -> dto.Client:
        pass

    @abstractmethod
    def register_new_user(self, login: str, password: str):
        pass


class AbstractCarProvider(ABC):
    @abstractmethod
    def get_all_cars(self):
        pass


class SqliteDataProvider(AbstractClientProvider, AbstractCarProvider):
    _provider = None

    def __init__(self):
        self._db = SqliteDatabaseProvider()

    @classmethod
    def get_provider(cls):
        if not cls._provider:
            cls._provider = SqliteDataProvider()
        return cls._provider

    def is_login_exist(self, login: str) -> bool:
        sql = f'''
        SELECT EXISTS (
	SELECT c.id
	from client c 
	where c.login = '{login}'
);
        '''
        res = self._db.execute_select(sql)
        return bool(int(res[0][0]))

    def check_password(self, login: str, password: str) -> bool:
        sql = f'''SELECT c.password = '{password}'
FROM client c 
WHERE c.login = '{login}';
'''
        res = self._db.execute_select(sql)
        return bool(int(res[0][0]))

    def get_client(self, login: str) -> dto.Client:
        sql = f'''
        SELECT *
from client c 
where c.login = '{login}' or c.id = '{login}';
'''
        return converter.DbResponseToClientConverter().convert(data=self._db.execute_select(sql)[0])

    def register_new_user(self, login: str, password: str) -> dto.Client:
        sql = f'''
        INSERT INTO client (login, password) VALUES
("{login}", "{password}")
        '''
        self._db.execute_update(sql)
        return self.get_client(login)

    def get_all_cars(self):
        sql = f'''SELECT a.id, a.produceyear, e.name, e2.name, g.name, a.enginevolume, c.name, f.name, a.model, a.horsepower, a.baterycapacity 
FROM auto a 
join equipment e on e.id  = a.equipmentid 
join enginetype e2 on e2.id = a.enginetypeid 
join gearbox g on g.id = a.gearboxtypeid
join cartype c on c.id  = a.cartypeid 
join firm f on f.id = a.firmid 
        '''

        res = self._db.execute_select(sql)
        return [converter.DbResponseToCarConverter().convert(data=row) for row in res]
