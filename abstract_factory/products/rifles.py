from abc import ABC, abstractmethod

# Abstract Product
class Rifle(ABC):
    @abstractmethod
    def shoot(self) -> str:
        pass

# Concrete Products
class AK47(Rifle):
    def shoot(self) -> str:
        return "AK-47: One tap headshot potential!"

class M4A1(Rifle):
    def shoot(self) -> str:
        return "M4A1-S: Silent and precise rifle!"