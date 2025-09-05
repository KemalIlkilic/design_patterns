from factory_method_design_pattern.abstract.logistic import Logistic
from factory_method_design_pattern.concrete.truck import Truck


class RoadLogistic(Logistic):

    def create_transport(self) -> Truck:
        return Truck()