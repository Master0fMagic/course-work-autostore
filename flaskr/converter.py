from abc import ABC, abstractmethod
import dto


class AbstractConverter(ABC):
    @abstractmethod
    def convert(self, **kwargs):
        pass


class DbResponseToClientConverter(AbstractConverter):

    def convert(self, **kwargs):
        """
        kwargs:
            data: list|set|tuple with db result
        """

        if 'data' not in kwargs:
            raise KeyError('"data" is not present in kwargs')

        return dto.Client(*kwargs['data'])


class DbResponseToCarConverter(AbstractConverter):
    def convert(self, **kwargs):
        """
        kwargs:
            data: list|set|tuple with db result
        """

        if 'data' not in kwargs:
            raise KeyError('"data" is not present in kwargs')

        return dto.Car(*kwargs['data'])


class DbResponseToTestDriveConverter(AbstractConverter):
    def convert(self, **kwargs):
        """
        kwargs:
            data: list|set|tuple with db result
        """

        if 'data' not in kwargs:
            raise KeyError('"data" is not present in kwargs')

        return dto.TestDrive(*kwargs['data'])


class DbResponseToFilterConverter(AbstractConverter):
    def convert(self, **kwargs):
        """
        kwargs:
            data: list|set|tuple with db result
        """

        if 'data' not in kwargs:
            raise KeyError('"data" is not present in kwargs')

        return dto.FilterItem(*kwargs['data'])


class DbResponseToDealerCenterConverter(AbstractConverter):
    def convert(self, **kwargs):
        """
        kwargs:
            data: list|set|tuple with db result
        """

        if 'data' not in kwargs:
            raise KeyError('"data" is not present in kwargs')

        return dto.DealerCenter(*kwargs['data'])
