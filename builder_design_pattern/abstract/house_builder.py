from abc import ABC, abstractmethod
from .house import House

class HouseBuilder(ABC):

    @property
    @abstractmethod # This is a property that returns a House object
    def house(self) -> House:
        pass

    @abstractmethod
    def set_floors(self) -> None:
        pass

    @abstractmethod
    def set_walls(self) -> None:
        pass
    
    @abstractmethod
    def set_house_name(self, name: str) -> None:
        pass