from .abstract_factory import GunFactory
from ..products.pistols import FiveSeven
from ..products.rifles import M4A1

class CTGunFactory(GunFactory):
    def create_pistol(self):
        return FiveSeven()

    def create_rifle(self):
        return M4A1()