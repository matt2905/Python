import dataclasses
import random
from typing import ClassVar


@dataclasses.dataclass
class Person:
    _name: str
    _health: int
    strength: ClassVar[int] = 25

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, newHP):
        self._health = newHP

    def take_damage(self, damage):
        self.health -= damage

    def do_turn(self, challenger):
        damage = random.randint(1, self.__class__.strength)
        print(self, "attack for:", damage)
        challenger.take_damage(damage)

    def fight(self, challenger):
        print("=" * 100, "\nFight between:\n")
        print("Fight between:")
        print("    ", self)
        print("    ", challenger)
        print("=" * 100)
        while 1:
            self.do_turn(challenger)
            if challenger.health <= 0:
                break
            challenger.do_turn(self)
            if self.health <= 0:
                break

    def __repr__(self):
        s = ', '.join(f'{field.name}={getattr(self, field.name)}'
                      for field in dataclasses.fields(self))
        s += f', strength={self.__class__.strength}'
        return f'{self.__class__.__name__}({s})'
