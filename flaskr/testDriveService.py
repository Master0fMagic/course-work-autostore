from abc import ABC, abstractmethod
import provider
from util import DateUtil
import error


class AbstractTestDriveService(ABC):
    _provider: provider.AbstractTestDriveProvider

    @abstractmethod
    def create_test_drive(self, car_id: int, date: int, client_id: int):
        pass


class TestDriveService(AbstractTestDriveService):
    def __init__(self):
        self._provider = provider.SqliteDataProvider.get_provider()

    def create_test_drive(self, car_id: int, date: int, client_id: int):
        test_drive_day = DateUtil.truncate_to_day(date)

        if self._provider.check_car(car_id, test_drive_day, client_id):
            raise error.CarIsBookedOrUserIsBusyException()
        self._provider.create_test_drive(car_id, test_drive_day, client_id)
