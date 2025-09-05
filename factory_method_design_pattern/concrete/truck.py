from factory_method_design_pattern.abstract.transport import Transport


class Truck(Transport):
    def deliver(self) -> str:
        return "Delivered by Truck"