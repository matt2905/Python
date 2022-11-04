import dataclasses
from typing import ClassVar
from person import Person


@dataclasses.dataclass
class Farmer(Person):
    strength: ClassVar[int] = 50

    def __repr__(self):
        return super().__repr__()
