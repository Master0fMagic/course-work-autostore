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
    def get_all_cars(self) -> list[dto.Car]:
        pass

    @abstractmethod
    def get_filter_values(self, filter_name: str) -> list[dto.FilterItem]:
        pass


class AbstractTestDriveProvider(ABC):
    @abstractmethod
    def create_test_drive(self, car_id: int, date: int, client_id: int):
        pass

    @abstractmethod
    def check_car(self, car_id: int, date: int, client_id: int) -> bool:
        pass

    @abstractmethod
    def get_test_drives_by_client(self, client_id: int) -> list[dto.TestDrive]:
        pass


class SqliteDataProvider(AbstractClientProvider, AbstractCarProvider, AbstractTestDriveProvider):
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
        SELECT c.id , c.login , c.password 
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

    def get_all_cars(self) -> list[dto.Car]:
        sql = '''SELECT a.id, a.produceyear, e.name, e2.name, g.name, a.enginevolume, c.name, f.name, a.model, a.horsepower, a.baterycapacity 
FROM auto a 
join equipment e on e.id  = a.equipmentid 
join enginetype e2 on e2.id = a.enginetypeid 
join gearbox g on g.id = a.gearboxtypeid
join cartype c on c.id  = a.cartypeid 
join firm f on f.id = a.firmid 
        '''

        res = self._db.execute_select(sql)
        return [converter.DbResponseToCarConverter().convert(data=row) for row in res]

    def check_car(self, car_id: int, date: int, client_id: int) -> bool:
        sql = f'''SELECT EXISTS (
select id  
from testdrives t 
where (t.autoid = {car_id} or t.clientid = {client_id})
and t.testdrivedate = {date})
        '''
        res = self._db.execute_select(sql)
        return bool(int(res[0][0]))

    def create_test_drive(self, car_id: int, date: int, client_id: int):
        sql = f'''INSERT INTO testdrives(autoid, testdrivedate, clientid) VALUES
({car_id}, {date}, {client_id});'''

        self._db.execute_update(sql)

    def get_test_drives_by_client(self, client_id: int) -> list[dto.TestDrive]:
        sql = f'''SELECT a.produceyear || ' ' || f.name || ' ' || a.model, t.testdrivedate 
from testdrives t 
join auto a ON a.id = t.autoid 
join firm f ON f.id = a.firmid 
where t.clientid = {client_id}'''

        return [converter.DbResponseToTestDriveConverter().convert(data=item) for item in self._db.execute_select(sql)]

    def get_filter_values(self, filter_name: str) -> list[dto.FilterItem]:
        sql = f'''SELECT * from {filter_name}'''

        return [converter.DbResponseToFilterConverter().convert(data=item) for item in self._db.execute_select(sql)]
