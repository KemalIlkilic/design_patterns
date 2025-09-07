from __future__ import annotations
from ..abstract import ChessPiece
import copy


class Knight(ChessPiece):

    def __init__(self, material : str, height : int):
        self._material = material
        self._height = height
        self._can_move_diagonal = False
        self._can_move_straight = False
        self._can_move_l_shape = True

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, material: str) -> None:
        self._material = material

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    @property
    def can_move_diagonal(self) -> bool:
        return self._can_move_diagonal

    @property
    def can_move_straight(self) -> bool:
        return self._can_move_straight

    @property
    def can_move_l_shape(self) -> bool:
        return self._can_move_l_shape

    def clone(self) -> Knight:
        return copy.deepcopy(self)

    def __str__(self):
        return f"Knight (material: {self._material}, height: {self._height})"