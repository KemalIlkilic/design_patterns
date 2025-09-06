from ...abstract import House


class BigHouse(House):
    def get_type(self) -> str:
        return "BigHouse"