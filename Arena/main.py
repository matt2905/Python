from faker import Faker
from farmer import Farmer
from knight import Knight
from priest import Priest
import random
from sorcerer import Sorcerer
from warior import Warior


if __name__ == '__main__':
    classes = (Farmer, Warior, Knight, Sorcerer, Priest)

    arena = [random.choice(classes)(Faker().name(), 1000) for _ in range(10)]
    print("Champions inside arena")
    for champion in arena:
        print(champion)

    while 1:
        champion, challenger = random.sample(arena, 2)
        champion.fight(challenger)
        if champion.health <= 0:
            arena.remove(champion)
        elif challenger.health <= 0:
            arena.remove(challenger)

        if len(arena) == 1:
            print("=" * 100)
            print(arena[0], "is the winner")
            break
