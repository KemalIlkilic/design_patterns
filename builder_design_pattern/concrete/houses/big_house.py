from builder_design_pattern.abstract.house import House


class BigHouse(House):
    def get_type(self) -> str:
        return "BigHouse"