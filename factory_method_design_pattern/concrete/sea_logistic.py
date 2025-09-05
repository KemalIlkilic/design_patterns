
from factory_method_design_pattern.abstract.logistic import Logistic
from factory_method_design_pattern.concrete.ship import Ship


class SeaLogistic(Logistic):

    def create_transport(self) -> Ship:
        return Ship()