from __future__ import annotations

from abc import ABC, abstractmethod
#It is a prototype interface

class ChessPiece(ABC):
    @property
    @abstractmethod
    def can_move_diagonal(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def can_move_straight(self) -> bool:
        pass

    @property
    @abstractmethod
    def can_move_l_shape(self) -> bool:
        pass

    @abstractmethod
    def clone(self) -> ChessPiece:
        pass