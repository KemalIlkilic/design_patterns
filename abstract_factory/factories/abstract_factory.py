from abc import ABC, abstractmethod

class GunFactory(ABC):
    @abstractmethod
    def create_pistol(self):
        pass

    @abstractmethod
    def create_rifle(self):
        pass