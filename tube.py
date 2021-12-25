from __future__ import annotations

from colours import Colour

TubeContents = list[Colour | None]
Pour = tuple[Colour, int]

class Tube:
    __contents__: TubeContents
    __max_level__ = 4

    def __init__(self, initial_contents: TubeContents | None = None) -> None:
        if initial_contents == None:
            self.__contents__ = [None] * self.__max_level__
            return
        
        if len(initial_contents) != self.__max_level__:
            raise ValueError(f"Initial contents must have length {self.__max_level__}")
        
        self.__contents__ = initial_contents

    def __repr__(self) -> str:
        return self.__contents__.__repr__()

    def empty_spaces(self) -> int:
        empty = 0

        while empty < self.__max_level__:
            if self.__contents__[empty] == None:
                empty += 1
            else:
                break

        return empty

    def top_colour(self) -> Colour | None:
        empty = self.empty_spaces()
        
        if self.is_empty():
            return None
        
        return self.__contents__[empty]

    def is_empty(self) -> bool:
        return self.empty_spaces() == self.__max_level__

    def is_solid_colour(self) -> bool:
        if self.is_empty():
            return False

        return len(set(self.__contents__)) == 1

    def can_receive(self, pour: Pour) -> bool:
        if self.is_empty():
            return True

        (colour, amount) = pour

        return amount <= self.empty_spaces() and colour == self.top_colour()

    def will_pour(self) -> Pour | None:
        pour_colour = self.top_colour()

        if pour_colour == None:
            return None

        pour_amount = 1
        slot_to_check = self.empty_spaces() + 1

        while slot_to_check < self.__max_level__:
            if self.__contents__[slot_to_check] == pour_colour:
                pour_amount += 1
                slot_to_check += 1
            else:
                break

        return (pour_colour, pour_amount)

    def receive(self, pour: Pour) -> Tube:
        if not self.can_receive(pour):
            raise ValueError("Cannot receive pour")

        (colour, amount) = pour

        new_contents = self.__contents__.copy()
        slot_to_fill = self.empty_spaces() - 1

        while amount > 0:
            new_contents[slot_to_fill] = colour
            slot_to_fill -=1
            amount -= 1

        return Tube(new_contents)

    def pour_into(self, tube: Tube) -> tuple[Tube, Tube]:
        pour = self.will_pour()

        if pour == None:
            raise ValueError('Cannot pour because tube is empty')

        new_source_contents = self.__contents__.copy()
        
        (_, amount) = pour
        pour_from = self.empty_spaces()
        while amount > 0:
            new_source_contents[pour_from] = None
            pour_from += 1
            amount -= 1

        target_tube = tube.receive(pour)
        source_tube = Tube(new_source_contents) 

        return (source_tube, target_tube)
        

