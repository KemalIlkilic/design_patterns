from ..abstract import Logistic
from .truck import Truck


class RoadLogistic(Logistic):

    def create_transport(self) -> Truck:
        return Truck()