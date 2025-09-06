from . import TGunFactory, CTGunFactory, game_loadout


if __name__ == "__main__":
    print("Terrorist loadout:")
    game_loadout(TGunFactory())

    print("\nCounter-Terrorist loadout:")
    game_loadout(CTGunFactory())