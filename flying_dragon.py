from dragon import Dragon
import random
class FlyingDragon(Dragon):
    def __init__(self, name, max_hp, swoops):
        super().__init__(name, max_hp)
        self._swoops = 5

    def special_attack(self, other):
        if self._swoops > 0:
            if other.hp > 0:
                damage = random.randint(5, 8)
                other.take_damage(damage)
                self._swoops -= 1
            return str(f"{self._name} swoops at you for {damage} damage!")
        else:
            return str(f"{self._name} has no swoops left!")

    def __str__(self):
        return f"Swoop attacks remianing: {self._swoops}"
