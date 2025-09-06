from .abstract_factory import GunFactory
from ..products.pistols import Tec9
from ..products.rifles import AK47

class TGunFactory(GunFactory):
    def create_pistol(self):
        return Tec9()

    def create_rifle(self):
        return AK47()