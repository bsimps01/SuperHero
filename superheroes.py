import random

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength 

    def attack(self):
        return random.randint(0, self.max_damage)
