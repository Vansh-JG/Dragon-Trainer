import abc
class Entity:

    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    def take_damage(self, dmg):
        self._hp = self._hp - dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        print(f"{self._name}: {self._hp}/{self._max_hp}")

    @abc.abstractmethod
    def basic_attack(self, other):
        pass

    @abc.abstractmethod
    def special_attack(self, other):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

