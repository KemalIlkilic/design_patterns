from abc import ABC, abstractmethod

class House(ABC):
    def __init__(self):
        self.__floors = None
        self.__walls = None
        self.__house_name = None
    
    @abstractmethod
    def get_type(self) -> str:
        pass
    
    @property
    def floors(self) -> int:
        return self.__floors
    
    @floors.setter
    def floors(self, floors: int) -> None:
        self.__floors = floors
    
    @property
    def walls(self) -> int:
        return self.__walls
    
    @walls.setter
    def walls(self, walls: int) -> None:
        self.__walls = walls
    
    @property
    def house_name(self) -> str:
        return self.__house_name
    
    @house_name.setter
    def house_name(self, name: str) -> None:
        self.__house_name = name
    
    def __str__(self):
        name_part = f" '{self.__house_name}'" if self.__house_name else ""
        return f"{self.get_type()}{name_part}(floors={self.__floors}, walls={self.__walls})"