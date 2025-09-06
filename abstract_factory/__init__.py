from .factories import GunFactory, TGunFactory, CTGunFactory

def game_loadout(factory: GunFactory):
    pistol = factory.create_pistol()
    rifle = factory.create_rifle()
    print(pistol.shoot())
    print(rifle.shoot())

__all__ = ['GunFactory', 'TGunFactory', 'CTGunFactory', 'game_loadout']

