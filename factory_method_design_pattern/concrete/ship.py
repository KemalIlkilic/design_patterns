from factory_method_design_pattern.abstract.transport import Transport


class Ship(Transport):
    def deliver(self) -> str:
        return "Delivered by Ship"