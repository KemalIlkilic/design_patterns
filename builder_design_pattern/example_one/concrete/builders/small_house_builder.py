from builder_design_pattern.example_one.abstract.house_builder import HouseBuilder
from builder_design_pattern.example_one.concrete.houses.small_house import SmallHouse


class SmallHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._house = SmallHouse()

    @property
    def house(self) -> SmallHouse:
        """
        Various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body.
        """

        product = self._house
        self.reset()
        return product
    
    def set_floors(self) -> None:
        self._house.floors = 2
        return self
    
    def set_walls(self) -> None: 
        self._house.walls = 5
        return self
    
    def set_house_name(self, name: str) -> None:
        self._house.house_name = name
        return self