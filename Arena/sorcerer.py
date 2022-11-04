import dataclasses
import random
from person import Person


@dataclasses.dataclass
class Sorcerer(Person):
    def __init__(self, name, HP):
        super().__init__(name, HP)
        self.mana = 100

    def do_turn(self, challenger):
        damage = 0
        if self.mana >= 10:
            mana_used = random.randint(0, 10)
            damage = self.__class__.strength * (mana_used // 2)
            self.mana -= mana_used
        else:
            damage = random.randint(0, self.__class__.strength)
        print(self, "attack for:", damage)
        challenger.take_damage(damage)

    def __repr__(self):
        s = ', '.join(f'{field.name}={getattr(self, field.name)}'
                      for field in dataclasses.fields(self))
        s += f', strength={self.__class__.strength}'
        s += f', mana={self.mana}'
        return f'{self.__class__.__name__}({s})'
