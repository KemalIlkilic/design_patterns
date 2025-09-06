from .abstract import Logistic
from .concrete import RoadLogistic, SeaLogistic

def client_code(creator: Logistic) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.do_delivery()}", end="")

__all__ = ['RoadLogistic', 'SeaLogistic','client_code']