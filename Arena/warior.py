import dataclasses
from typing import ClassVar
from person import Person


@dataclasses.dataclass
class Warior(Person):
    strength: ClassVar[int] = 100

    def __repr__(self):
        return super().__repr__()
