from abc import ABC, abstractmethod

# Abstract Product
class Pistol(ABC):
    @abstractmethod
    def shoot(self) -> str:
        pass

# Concrete Products
class Tec9(Pistol):
    def shoot(self) -> str:
        return "Tec-9: Rapid fire with low accuracy!"

class FiveSeven(Pistol):
    def shoot(self) -> str:
        return "Five-SeveN: Accurate pistol with armor penetration!"