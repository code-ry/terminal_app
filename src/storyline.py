from random import randint
import time
import numpy as np

# class Levels:
#     def __init__(self, level1, level2):

    
#         self.levels = [level1, level2]
#         self.level_selector = -1

#     def add_level(self, level):
#         self.levels.append(level)
    
#     def next_level(self):
#         self.level_selector += 1
#         return self.levels[self.level_selector]
def get_input(prompt):
    input_value = input(prompt)

    if input_value == "quit":
        raise KeyboardInterrupt
    
    return input_value

class StoryChoice:
    def __init__(self, question, answer, alt = 'Y'):
        self.question = question
        self.answer = answer
        self.progress = True
        self.alt = alt

    def choice(self):
        answer = get_input(f'{self.question}')
        if answer in (self.answer, self.alt):
            self.progress = True
        else:
            self.progress = False

class Player:
    hero_list = np.array(['a', 'b', 'c'])
    hero = ''
    items = {'Ring of health' : 20, 'Ring of Attack' : 40}

    def set(self):
        if self.hero == 'a':
            self.name = 'Grimly The Fierce'
            self.hp = 100
            self.attack = 10
            self.weapon = 'swings their mighty Axe'

        elif self.hero == 'b':
            self.name = 'Ethondril the Agile'
            self.hp = 60
            self.attack = 20
            self.weapon = 'fires their Long-Bow'

        else:
            self.name = 'Ailwyn the Powerful'
            self.hp = 50
            self.attack = 40
            self.weapon = 'launches a devestating Frostbolt'

    def hero_pick(self):

        while self.hero not in self.hero_list:
                
                self.hero = get_input('Which hero would you like to play as?\n a. Grimly The Fierce a Warrior\n b. Ethondril the Agile an Archer\n c. Ailwyn the Powerful a Wizard\n')

    def __repr__(self):
        return f'{self.hero}, {self.hp}, {self.attack}, {self.weapon}'

    def battle(self, enemy):
        input(f'You face off with the {enemy.name}.\n You must roll a higher number to attack. Press enter to roll!')
        counter = 0
        while self.hp > 0 and enemy.hp > 0:
            # item_add = input('Would you like to use an item?')
            # if item_add == 'Y':
            #     which_item = input(f'Which item would you like to use?{self.items[')
            #     self.attack += 20
            # if item_add == 'Y':

            if counter > 0:
                input('Press enter to Roll again!')
            counter += 1
            time.sleep(1)
            player_roll = randint(1,10)
            print(f'{self.name} rolls a {player_roll}')
            time.sleep(1)
            enemy_roll = randint(1,10)
            print(f'{enemy.name} rolls a {enemy_roll}')
            time.sleep(1)
            if player_roll > enemy_roll:
                enemy.hp -= self.attack
                print(f'{self.name} attacks and {self.weapon}.\n The {enemy.name} loses {self.attack} health with {enemy.hp} remaining.')
            elif enemy_roll > player_roll:
                self.hp -= enemy.attack
                print(f'{enemy.name} attacks and {enemy.weapon}.\n {self.name} loses {enemy.attack} health with {self.hp} remaining.')
            else:
                print('It\'s a Draw, roll again!')
            time.sleep(1)
            #     self.attack -= 20
            #     item_add == 'N'
        if self.hp > 0:
            print('You are the winner!')
        else:
            print('You are the Loser!')
        
    def puzzle(self):
        riddles = np.array([
            'What has to be broken before you can use it?',
            'I\'m tall when young yet short when I\'m old, What am I?',
            'I\'m full of holes but still hold water?'
            ])
        clues = np.array([
            'Who first, me or the Chicken!',
            'I show you the way in the dark!',
            'My best friend is Patrick!'
        ])
        answers = ['Egg', 'Candle', 'Sponge']
        attempts = 5
        x = randint(0, 2)
        while attempts > 0:
            player_answer = input(riddles[x])
            if player_answer in answers[x]:
                print('You Win!')
                break
            attempts -= 1
            if attempts < 3:
                print(f'Ok I will give you a clue... {clues[x]}')

class Monster:
    def __init__(self, name, hp, attack, weapon):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.weapon = weapon

