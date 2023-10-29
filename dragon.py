from entity import Entity
import random
class Dragon(Entity):
  def basic_attack(self, other):
    if other.hp > 0:
      damage = random.randint(3, 7)
      other.take_damage(damage)
    return str(f"{self._name} smashes you with its tail for {damage} damage!")

  def special_attack(self, other):
    if other.hp > 0:
      damage = random.randint(4, 8)
      other.take_damage(damage)
    return str(f"{self._name} slashes you with its claws for {damage} damage!")


