from ..abstract import Transport


class Truck(Transport):
    def deliver(self) -> str:
        return "Delivered by Truck"