from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self, name, max_hp, f_shots):
        super().__init__(name, max_hp)
        self.f_shots = 3

    def special_attack(self, other):
        if self.f_shots > 0:
            if other.hp > 0:
                damage = random.randint(5, 9)
                other.take_damage(damage)
                self.f_shots -= 1
            return str(f"{self._name} engulfs you in flames for {damage} damage!")
        else:
            return str(f"{self._name} is out of fire shots!")

    def __str__(self):
        return f"Fire shots remaining: {self.f_shots}"

