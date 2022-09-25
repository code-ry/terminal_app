import time
from random import randint
import numpy as np

# Checks input and makes first letter capital for consistency of input
# Raises KeyoardInterrupt if 'Quit' is entered to exit program

def get_input(prompt):
    input_value = input(prompt).capitalize()

    if input_value == "Quit":
        raise KeyboardInterrupt
    
    return input_value

# Creates IncorrectValue exception to use in exception function

class IncorrectValue(Exception):
    pass

# Checks if input value is not desired input value

def raise_exception(input_value=None, val_one = None, val_two = None, val_three = None):
    if input_value not in (val_one, val_two, val_three):
        raise IncorrectValue

# Basic storyline creation and concatenation

class StoryLine:
    def __init__(self, line):
        self.lines = [line]

    def add_line(self, line):
        self.lines.append(line)
    
    def concat_lines(self):
        for i in self.lines:
            print(i)
            time.sleep(2)

# Storyline creation which can randomly generate one line.

class DeathMessage():
    def __init__(self, message):
        self.messages = [message]
        self.base_messages = [message]

    def add_line(self, message):
        self.messages.append(message)
        self.base_messages.append(message)
    
    # Selects random message from list and removes after displaying to terminal

    def random_death(self):
        i = randint(0, len(self.messages) - 1)
        print(self.messages[i])
        self.messages.pop(i)

        #When list is exhausted, replenishes with original list.

        if len(self.messages) - 1 == 0:
            self.messages = self.base_messages

# Storyline creation which provides an input option and saves as variable to control flow

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
            print(f'\n{user_input} is not a valid value.\n')

        while user_input not in (self.path_one, self.path_two):
            print(f'Please enter either {self.path_one} or {self.path_two}\n')
            user_input = get_input(f'{self.question}')
            
        if user_input == self.path_one:
            self.progress = True
        else:
            self.progress = False

# Storyline option that terminates program if one path is chosen (to exit)
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

        if user_input == self.path_two:
            raise KeyboardInterrupt
     

# Simple character creation

class Character:
    def __init__(self, name, base_hp, attack, weapon):
        self.name = name
        self.base_hp = base_hp
        self.attack = attack
        self.weapon = weapon
        self.hp = base_hp

# Player specific character creation

class Player(Character):
    def __init__(self, name=None, base_hp=None, attack=None, weapon=None):
        super().__init__(name, base_hp, attack, weapon)
        self.name = name
        self.base_hp = base_hp
        self.attack = attack
        self.weapon = weapon
        self.hp = base_hp
        self.badges = []

    # player Hero selection

    def hero_pick(self, hero_one, hero_two, hero_three):
        user_input = get_input(f'''\nWhich hero would you like to play as?\n 
        A. {hero_one.name} | Health: {hero_one.base_hp} | Attack: {hero_one.attack} | Weapon: {hero_one.weapon}\n
        B. {hero_two.name} | Health: {hero_two.base_hp} | Attack: {hero_two.attack} | Weapon: {hero_two.weapon}\n
        C. {hero_three.name} | Health: {hero_three.base_hp} | Attack: {hero_three.attack} | Weapon: {hero_three.weapon}\n''')

        while user_input not in ('A', 'B', 'C'):
            try:
                raise_exception(user_input, 'A', 'B', 'C')

            except IncorrectValue:
                print(f'{user_input} is not a valid value.\n')
                
            user_input = get_input('Please enter either A, B or C: \n')
        
        if user_input == 'A':
            self.name = hero_one.name
            self.base_hp = hero_one.base_hp
            self.attack = hero_one.attack
            self.weapon = hero_one.weapon
            self.hp = hero_one.hp
            self.badges = []
        
        elif user_input == 'B':
            self.name = hero_two.name
            self.base_hp = hero_two.base_hp
            self.attack = hero_two.attack
            self.weapon = hero_two.weapon
            self.hp = hero_two.hp
            self.badges = []

        if user_input == 'C':
            self.name = hero_three.name
            self.base_hp = hero_three.base_hp
            self.attack = hero_three.attack
            self.weapon = hero_three.weapon
            self.hp = hero_three.hp
            self.badges = []
            
    def __repr__(self):
        return f'{self.name}, {self.hp}, {self.attack}, {self.weapon}'
