import math

# ----------------------
# Round system (compatible)
# ----------------------
class RoundHole:
    def __init__(self, radius: float):
        self._radius = radius

    def get_radius(self) -> float:
        return self._radius

    def fits(self, peg: "RoundPeg") -> bool:
        return self.get_radius() >= peg.get_radius()


class RoundPeg:
    def __init__(self, radius: float):
        self._radius = radius

    def get_radius(self) -> float:
        return self._radius


# ----------------------
# Square system (incompatible)
# ----------------------
class SquarePeg:
    def __init__(self, width: float):
        self._width = width

    def get_width(self) -> float:
        return self._width


# ----------------------
# Adapter: makes SquarePeg compatible with RoundPeg
# ----------------------
class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg: SquarePeg):
        # SquarePeg is wrapped inside
        self._square_peg = square_peg

    def get_radius(self) -> float:
        # Convert square width to equivalent circle radius
        return (self._square_peg.get_width() * math.sqrt(2)) / 2


# ----------------------
# Client code
# ----------------------
if __name__ == "__main__":
    hole = RoundHole(5)

    rpeg = RoundPeg(5)
    print(hole.fits(rpeg))  # True

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)

    # This wouldn't work: hole.fits(small_sqpeg)  # ❌ incompatible

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

    print(hole.fits(small_sqpeg_adapter))  # True ✅
    print(hole.fits(large_sqpeg_adapter))  # False ❌