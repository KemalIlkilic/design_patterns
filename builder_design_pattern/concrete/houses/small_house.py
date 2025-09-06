from ...abstract import House


class SmallHouse(House):
    def get_type(self) -> str:
        return "SmallHouse"