import dataclasses
from typing import ClassVar
from person import Person


@dataclasses.dataclass
class Knight(Person):
    strength: ClassVar[int] = 75
    defense: ClassVar[int] = 25

    def take_damage(self, damage):

        print(f'{self} reduced incomming damage by {Knight.defense}')
        self.health -= max((damage - Knight.defense), 0)

    def __repr__(self):
        s = ', '.join(f'{field.name}={getattr(self, field.name)}'
                      for field in dataclasses.fields(self))
        s += f', strength={self.__class__.strength}'
        s += f', defense={self.__class__.defense}'
        return f'{self.__class__.__name__}({s})'
