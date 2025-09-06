from .concrete import SeaLogistic
from .concrete import RoadLogistic
from . import client_code


if __name__ == "__main__":
    print("App: Launched with the Sea Logistic ")
    sea_logistic = SeaLogistic()
    client_code(sea_logistic)
    print("\n")

    print("App: Launched with the Road Logistic ")
    client_code(RoadLogistic())