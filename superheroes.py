import random
import sys

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
        self.current_health = 100
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
        # if len(opponent.abilities) == 0 and len(self.abilities) == 0:
        #     return "It's a Draw!"
        # else :     
        while self.is_alive() and opponent.is_alive():
            if len(self.abilities) > 0 and len(opponent.abilities) == 0 :
                opponent.take_damage(self.attack())
            elif len(opponent.abilities) > 0 and len(self.abilities) == 0 :
                self.take_damage(opponent.attack())
            else:
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
        # team_one_alive = []
        # team_two_alive = []

        # for hero1 in self.heroes:
        #     if hero1.is_alive() == True:
        #         team_one_alive.append(self.heroes.index(hero1))
        
        # for hero2 in other_team.heroes:
        #     if hero2.is_alive() == True:
        #         team_two_alive.append(other_team.heroes.index(hero2))

        #     team_one_hero = random.choice(team_one_alive)
        #     team_two_hero = random.choice(team_two_alive)
        #     team_one_hero.fight(team_two_hero)

        #     if not team_one_hero.is_alive():
        #         team_one_alive.remove(team_one_hero)
        #     elif not team_two_hero.is_alive():
        #         team_two_alive.remove(team_two_hero)
        random_hero = random.choice(self.heroes)
        other_random_hero = random.choice(other_team.heroes)
        while random_hero.is_alive() and other_random_hero.is_alive():
            random_hero.fight(other_random_hero)

    def currently_alive(self):
        currently_alive = []
        for hero in self.heroes:
            if hero.is_alive == True:
                currently_alive.append(hero)
            return currently_alive

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

class Arena:
    def __init__(self):
        self.winning_team = None
        print('\nWelcome to the League of Champions\n')
        self.team1 = input('What is the name of the first squad? ')
        self.team_one = Team(self.team1)
        self.team2 = input('What do you want the second squad to be called? ')
        self.team_two = Team(self.team2)

    def create_weapon(self):
        weapon_name = input("Weapon name: ")
        max_damage = input("Max weapon damage: ")
        return Weapon(weapon_name, int(max_damage))

    def create_ability(self):
        ability_name = input("Ability name: ")
        max_damage = input("Max damage: ")
        return Ability(ability_name, int(max_damage))

    def create_armor(self):
        armor_name = input("Armor name: ")
        armor_block = input("Max armor block: ")
        return Armor(armor_name, int(armor_block))

    def create_hero(self):
        hero_name = input('Choose a name for your hero: ')
        health = input('How about some hp? Default is 100: ')
        hero = Hero(hero_name, health)

        add_abilities = input('\nDoes your hero have any abilities? y/n ')
        if 'y' in add_abilities:
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)

                more_abilities = input('Want to add another ability? y/n ')
                if 'y' not in more_abilities:
                    break
    
        add_weapons = input('\nDo they have weapons? y/n ')
        if 'y' in add_weapons:
            while True:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)

                more_weapons = input('Want to add another weapon? y/n ')
                if 'y' not in more_weapons:
                    break

        add_armor = input('\nDoes your hero have any armor? y/n ')
        if 'y' in add_armor:
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)

                more_armor = input('Want to add more armor? y/n \n')
                if 'y' not in more_armor:
                    break
        return hero
                
    def build_team_one(self):
        t1_num = input('How many hero(es) do you want on team 1? ')
        if t1_num.isalnum():
            for _ in range(0, int(t1_num)):
                hero = self.create_hero()
                self.team_one.add_hero(hero)
        else:
            t1_num = input('Incorrect input. Please enter a number: ')
            return t1_num

    def build_team_two(self):
        t2_num = input('How many hero or heroes do you want on the second squad? ')
        if t2_num.isalnum():
            for _ in range(0, int(t2_num)):
                hero = self.create_hero()
                self.team_two.add_hero(hero)
        else:
            t2_num = input('Incorrect input. Please enter a number: ')
            exit()
            
    def team_battle(self):
        ''' Puts team one against team two '''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\nStats: ")
        self.team_one.stats()
        self.team_two.stats()
        if len(self.team_one.currently_alive()) > 0:
            print(self.team1 + "win")
        else:
            print(self.team2 + "win")

        #print("The winning team is: " + self.winning_team)

# if __name__ == "__main__":

#     hero = Hero("Spiderman")
#     opponent = Hero("Wonder Woman")
#     ability1 = Ability("Web Slinging", 50)
#     ability2 = Ability("Quick Agility", 150)
#     ability3 = Ability("Super Strength", 120)
#     ability4 = Ability("Lasso of Truth", 10)
#     hero.add_ability(ability1)
#     hero.add_ability(ability2)
#     opponent.add_ability(ability3)
#     opponent.add_ability(ability4)
#     hero.fight(opponent)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ").lower()

        #Check for Player Input
        if play_again == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()