from ..abstract import House
from ..abstract import HouseBuilder


class HouseDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> HouseBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: HouseBuilder) -> None:
        self._builder = builder

    def construct_house(self, name : str) -> House:
        self.builder.set_house_name(name)
        self.builder.set_floors()
        self.builder.set_walls()
        return self.builder.house