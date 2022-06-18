from abc import ABC, abstractmethod
import dto
import provider


class AbstractCarService(ABC):
    _provider: provider.AbstractCarProvider

    @abstractmethod
    def get_cars(self) -> list[dto.Car]:
        pass


class CarService(AbstractCarService):
    def __init__(self):
        self._provider = provider.SqliteDataProvider.get_provider()

    def get_cars(self) -> list[dto.Car]:
        return self._provider.get_all_cars()
