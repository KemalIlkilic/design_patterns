from builder_design_pattern.example_one.abstract.house import House


class BigHouse(House):
    def get_type(self) -> str:
        return "BigHouse"