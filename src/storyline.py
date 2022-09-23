import time
from random import randint
import numpy as np

def get_input(prompt):
    input_value = input(prompt).capitalize()

    if input_value == "Quit":
        raise KeyboardInterrupt
    
    return input_value

def raise_exception(input_value, val_one = None, val_two = None, val_three = None):
    if input_value not in (val_one, val_two, val_three):
        raise IncorrectValue

def random_death(val_one, val_two, val_three):
    messages = [val_one, val_two, val_three]
    i = randint(0, len(messages) - 1)
    print(messages[i])
    messages.pop(i)

class IncorrectValue(Exception):
    pass

class StoryLine:
    def __init__(self, line):
        self.lines = [line]

    def add_line(self, line):
        self.lines.append(line)
    
    def concat_lines(self):
        for i in self.lines:
            print(i)
            time.sleep(2)

class DeathMessage():
    def __init__(self, message):
        self.messages = [message]
        self.base_messages = [message]

    def add_line(self, message):
        self.messages.append(message)
        self.base_messages.append(message)
 
    def random_death(self):
        i = randint(0, len(self.messages) - 1)
        print(self.messages[i])
        self.messages.pop(i)

        if len(self.messages) - 1 == 0:
            self.messages = self.base_messages

class StoryChoice:
    def __init__(self, question, path_one, path_two):
        self.question = question
        self.path_one = path_one
        self.path_two = path_two
        self.progress = True


    def choice(self):
        user_input = get_input(f'{self.question}')
        try:
            raise_exception(user_input, self.path_one, self.path_two)
        except IncorrectValue:
            print('\nThis is not a valid value.\n')

        while user_input not in (self.path_one, self.path_two):
            print(f'Please enter either {self.path_one} or {self.path_two}\n')
            user_input = get_input(f'{self.question}')
            
        if user_input == self.path_one:
            self.progress = True
        else:
            self.progress = False

class PlayAgain(StoryChoice):
    def __init__(self, question, path_one, path_two):
        super().__init__(question, path_one, path_two)
        self.question = question
        self.path_one = path_one
        self.path_two = path_two
        self.progress = True
        
    def choice(self):
        user_input = get_input(f'{self.question}')
        while user_input not in (self.path_one, self.path_two):
            print(f'Please enter either {self.path_one} or {self.path_two} or \'quit\'.')
            user_input = get_input(f'{self.question}')

        if user_input == self.path_one:
            self.progress = True

        else:
            raise KeyboardInterrupt

class Character:
    def __init__(self, name, base_hp, attack, weapon):
        self.name = name
        self.base_hp = base_hp
        self.attack = attack
        self.weapon = weapon
        self.hp = base_hp

class Player(Character):
    def __init__(self, name=None, base_hp=None, attack=None, weapon=None):
        super().__init__(name, base_hp, attack, weapon)
        self.name = name
        self.base_hp = base_hp
        self.attack = attack
        self.weapon = weapon
        self.hp = base_hp

    hero = None
    hero_list = np.array(['A', 'B', 'C'])
    slayer_of_dragon = False
    master_of_riddles = False
    has_gem = False

    def hero_pick(self):
        user_input = get_input('\nWhich hero would you like to play as? \n A. Grimly The Fierce Warrior\n B. Ethondril the Agile Archer\n C. Ailwyn the Powerful Wizard\n')
        try:
            raise_exception(user_input, 'A', 'B', 'C')

        except IncorrectValue:
            print('This is not a valid value.\n')

        while user_input not in self.hero_list:
            user_input = get_input('Please enter either A, B or C: \n')
        
        self.hero = user_input

    def set(self):
        self.slayer_of_dragon = False
        self.master_of_riddles = False
        self.has_gem = False

        if self.hero == 'A':
            self.name = 'Grimly The Fierce'
            self.hp = 100
            self.attack = 30
            self.weapon = 'swings their mighty Axe'

        elif self.hero == 'B':
            self.name = 'Ethondril the Agile'
            self.hp = 60
            self.attack = 40
            self.weapon = 'fires their Long-Bow'

        else:
            self.name = 'Ailwyn the Powerful'
            self.hp = 20
            self.attack = 50
            self.weapon = 'launches a devestating Frostbolt'

    def __repr__(self):
        return f'{self.hero}, {self.hp}, {self.attack}, {self.weapon}'


  