from entity import Entity
import random

class Hero(Entity):
  def basic_attack(self, other):
    if other._hp > 0:
      damage = random.randint(1, 6) + random.randint(1, 6)
      other.take_damage(damage)
    return str(f"You slash the {other.name} with your sword for {damage} damage.")

  def special_attack(self, other):
    if other.hp > 0:
      damage = random.randint(1, 12)
      other.take_damage(damage)
    return str(f"You hit the {other.name} with an arrow for {damage} damage.")

