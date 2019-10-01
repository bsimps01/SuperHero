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

    def defend(self, damage_amt):
        blocks = 0
        for blocks in self.armors:
            blocks += damage_amt.block()
        return blocks

    def add_kill(self, num_kills):
        self.kills = num_kills

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_deaths(self, num_deaths):
        self.deaths = num_deaths

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        if len(opponent.abilities) == 0 and len(self.abilities) == 0:
            return "It's a Draw!"
        else :     
            while self.is_alive() and opponent.is_alive() :
                if len(self.abilities) > 0 and len(opponent.abilities) == 0 :
                    opponent.take_damage(self.attack())
                elif len(opponent.abilities) > 0 and len(self.abilities) == 0 :
                    self.take_damage(opponent.attack())
                else :
                    self.take_damage(opponent.attack())
                    opponent.take_damage(self.attack())
        
        if self.is_alive(): 
            print(f"{self.name} won!")
            opponent.add_deaths(1)
            self.add_kill(1)
        else :
            opponent.add_kill(1)
            self.add_deaths(1)            
            print(f"{opponent.name} won!")

"""if __name__== "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)"""

class Weapon(Ability):
    def __init__(self, name, attack_strength):
        super().__init__(name, attack_strength)

    def attack(self):
        return random.randint(0, self.max_damage)

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def attack(self, other_team):
        team_one_alive = []
        team_two_alive = []

        for hero1 in self.heroes:
            if hero1.is_alive() == True:
                team_one_alive.append(self.heroes.index(hero1))
        
        for hero2 in other_team.heroes:
            if hero2.is_alive() == True:
                team_two_alive.append(other_team.heroes.index(hero2))

        while len(team_one_alive) > 0 and len(team_two_alive) > 0:
            team_one_hero = random.choice(team_one_alive)
            team_two_hero = random.choice(team_two_alive)
            team_one_hero.fight(team_two_hero)

            if not team_one_hero.is_alive():
                team_one_alive.remove(team_one_hero)
            elif not team_two_hero.is_alive():
                team_two_alive.remove(team_two_hero)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                return 0

    def stats(self):
        for hero in self.heroes:
            print("Your Hero: {}".format(hero.name))
            print("Kills/Deaths: {}/{}".format(hero.kills, hero.deaths))

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

if __name__ == "__main__":

    hero = Hero("Spiderman")
    opponent = Hero("Wonder Woman")
    ability1 = Ability("Web Slinging", 50)
    ability2 = Ability("Quick Agility", 150)
    ability3 = Ability("Super Strength", 120)
    ability4 = Ability("Lasso of Truth", 10)
    hero.add_ability(ability1)
    hero.add_ability(ability2)
    opponent.add_ability(ability3)
    opponent.add_ability(ability4)
    hero.fight(opponent)