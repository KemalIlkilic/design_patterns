from ..abstract import Transport


class Ship(Transport):
    def deliver(self) -> str:
        return "Delivered by Ship"