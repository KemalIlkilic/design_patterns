from factory_method_design_pattern.abstract.logistic import Logistic
from factory_method_design_pattern.concrete.sea_logistic import SeaLogistic
from factory_method_design_pattern.concrete.road_logistic import RoadLogistic


def client_code(creator: Logistic) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.do_delivery()}", end="")


if __name__ == "__main__":
    print("App: Launched with the Sea Logistic ")
    sea_logistic = SeaLogistic()
    client_code(sea_logistic)
    print("\n")

    print("App: Launched with the Road Logistic ")
    client_code(RoadLogistic())