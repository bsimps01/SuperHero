import random

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength 

    def attack(self):
        return random.randint(0, self.max_damage)
"""if __name__ == "__main__":
    ability = Ability("debugging ability", 20)
    print(ability.name)
    print(ability.attack())"""

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0
    
    def add_ability(self, ability):
        self.abilities.append(ability) 

    def attack(self):
        hits = 0
        for hit in self.abilities:
            hits += hit.attack()
        return hits

    def add_kill(self, num_kills):
        self.kills = num_kills

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_deaths(self, num_deaths):
        self.deaths = num_deaths

    def defend(self, damage_amt):
        blocks = 0
        for blocks in self.armors:
            blocks += damage_amt.block()
        return blocks

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        self.opponent = opponent
        while self.is_alive() and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                self_attack = hero.attack()
                opponent_attack = opponent.attack()
                self.take_damage(opponent_attack)
                opponent.take_damage(self_attack)

                if self.is_alive == False:
                    print("The winner is: {}!".format(opponent.name))
                else:
                    print("The winner is: {}!".format(self.name))
            else:
                print("It ends in a Draw!")


"""if __name__== "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)"""

class Weapon(Ability):
    def __init__(self, name, attack_strength):
        super().__init__(name, attack_strength)

    def attack(self):
        return random.randint(0, self.max_damage)

if __name__ == "__main__":

    hero = Hero("Spiderman")
    opponent = Hero("Wonder Woman")
    ability1 = Ability("Web Slinging", 50)
    ability2 = Ability("Quick Agility", 150)
    ability3 = Ability("Super Strength", 120)
    ability4 = Ability("Lasso of Truth", 80)
    hero.add_ability(ability1)
    hero.add_ability(ability2)
    opponent.add_ability(ability3)
    opponent.add_ability(ability4)
    hero.fight(opponent)