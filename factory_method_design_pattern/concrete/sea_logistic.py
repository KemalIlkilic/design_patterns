
from ..abstract import Logistic
from .ship import Ship


class SeaLogistic(Logistic):

    def create_transport(self) -> Ship:
        return Ship()