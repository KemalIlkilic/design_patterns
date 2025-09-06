from ...abstract import HouseBuilder
from ...concrete import BigHouse


class BigHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self._house = BigHouse()

    @property
    def house(self) -> BigHouse:
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
        self._house.floors = 4
        return self
    
    def set_walls(self) -> None: 
        self._house.walls = 10
        return self
    
    def set_house_name(self, name: str) -> None:
        self._house.house_name = name
        return self