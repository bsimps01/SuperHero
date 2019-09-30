import random

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength 

    def attack(self):
        return random.randint(0, self.max_damage)
if __name__ == "__main__":
    ability = Ability("debugging ability", 20)
    print(ability.name)
    print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, current_health, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = current_health

if __name__== "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

class Weapon(Ability):
    def __init__(self, name, attack_strength):
        super().__init__(name, attack_strength)