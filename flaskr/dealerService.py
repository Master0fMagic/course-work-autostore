from abc import ABC, abstractmethod
import provider
import dto


class AbstractDealerService(ABC):
    _provider: provider.AbstractDealerCenterProvider

    @abstractmethod
    def get_dealer_centers(self) -> list[dto.DealerCenter]:
        pass

    @abstractmethod
    def get_dealer_center_by_car(self, car_id) -> list[dto.DealerCenter]:
        pass


class DealerService(AbstractDealerService):
    def get_dealer_center_by_car(self, car_id) -> list[dto.DealerCenter]:
        return self._provider.get_dealer_centers_by_car(car_id)

    def get_dealer_centers(self) -> list[dto.DealerCenter]:
        return self._provider.get_centers()

    def __init__(self):
        self._provider = provider.SqliteDataProvider.get_provider()
