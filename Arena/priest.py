import dataclasses
import random
from person import Person


@dataclasses.dataclass
class Priest(Person):
    def __init__(self, name, HP):
        super().__init__(name, HP)
        self.mana = 100

    def do_turn(self, challenger):
        super().do_turn(challenger)
        if (self.mana >= 10):
            heal = random.randint(0, 15)
            self.health += heal
            self.mana -= heal
            print(self, "regenerate for:", heal)

    def __repr__(self):
        s = ', '.join(f'{field.name}={getattr(self, field.name)}'
                      for field in dataclasses.fields(self))
        s += f', strength={self.__class__.strength}'
        s += f', mana={self.mana}'
        return f'{self.__class__.__name__}({s})'
