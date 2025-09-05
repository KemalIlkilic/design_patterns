from builder_design_pattern.abstract.house import House


class SmallHouse(House):
    def get_type(self) -> str:
        return "SmallHouse"