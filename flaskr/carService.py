from abc import ABC, abstractmethod
import dto
import provider


class AbstractCarService(ABC):
    _provider: provider.AbstractCarProvider

    @abstractmethod
    def get_cars(self) -> list[dto.Car]:
        pass

    @abstractmethod
    def get_equipment_filter(self) -> list[dto.FilterItem]:
        pass

    @abstractmethod
    def get_engine_type_filter(self) -> list[dto.FilterItem]:
        pass

    @abstractmethod
    def get_gearbox_filter(self) -> list[dto.FilterItem]:
        pass

    @abstractmethod
    def get_car_type_filter(self) -> list[dto.FilterItem]:
        pass

    @abstractmethod
    def get_firm_filter(self) -> list[dto.FilterItem]:
        pass


class CarService(AbstractCarService):
    def get_equipment_filter(self) -> list[dto.FilterItem]:
        return self._provider.get_filter_values(CarService.__EQUIPMENT)

    def get_engine_type_filter(self) -> list[dto.FilterItem]:
        return self._provider.get_filter_values(CarService.__ENGINE)

    def get_gearbox_filter(self) -> list[dto.FilterItem]:
        return self._provider.get_filter_values(CarService.__GEARBOX)

    def get_car_type_filter(self) -> list[dto.FilterItem]:
        return self._provider.get_filter_values(CarService.__CAR_TYPE)

    def get_firm_filter(self) -> list[dto.FilterItem]:
        return self._provider.get_filter_values(CarService.__FIRM)

    __FIRM = 'firm'
    __CAR_TYPE = 'cartype'
    __GEARBOX = 'gearbox'
    __ENGINE = 'enginetype'
    __EQUIPMENT = 'equipment'

    def __init__(self):
        self._provider = provider.SqliteDataProvider.get_provider()

    def get_cars(self) -> list[dto.Car]:
        return self._provider.get_all_cars()
