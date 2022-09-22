from random import randint
import time
import numpy as np

def get_input(prompt):
    input_value = input(prompt).capitalize()

    if input_value == "Quit":
        raise KeyboardInterrupt
    
    return input_value

class StoryChoice:
    def __init__(self, question, path_one, path_two, death_message):
        self.question = question
        self.path_one = path_one
        self.path_two = path_two
        self.progress = True
        self.death_message = death_message

    def choice(self):
        user_input = get_input(f'{self.question}')
        while user_input not in (self.path_one, self.path_two):
            print(f'Please enter either {self.path_one} or {self.path_two}')
            user_input = get_input(f'{self.question}')
        if user_input == self.path_one:
            self.progress = True
        else:
            self.progress = False

class PlayAgain(StoryChoice):
    def __init__(self, question, path_one, path_two):
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

class StoryLine:
    def __init__(self, line):
        self.line = [line]

    def add_line(self, line):
        self.line.append(line)
    
    def concat_lines(self):
        for i in self.line:
            print(i)
            time.sleep(2)

class Player:
    hero_list = np.array(['A', 'B', 'C'])
    hero = ''
    master_of_riddles = False
    has_gem = False

    def set(self):
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

    def hero_pick(self):
        self.hero = get_input('\nWhich hero would you like to play as? \n A. Grimly The Fierce Warrior\n B. Ethondril the Agile Archer\n C. Ailwyn the Powerful Wizard\n')
        while self.hero not in self.hero_list:
            self.hero = get_input('Please enter either a, b or c: ')          

    def __repr__(self):
        return f'{self.hero}, {self.hp}, {self.attack}, {self.weapon}'

    def battle(self, enemy):
        get_input(f'\nYou face off with the {enemy.name}.\nYou must roll a higher number than {enemy.name} to attack. Press enter to roll!\n')
        counter = 0
        enemy.hp = enemy.base_hp
        while self.hp > 0 and enemy.hp > 0:
            if counter > 0:
                get_input('\nPress enter to Roll again!\n')
            counter += 1
            time.sleep(1)
            player_roll = randint(1,10)
            print(f'{self.name} rolls a {player_roll}\n')
            time.sleep(1)
            enemy_roll = randint(1,10)
            print(f'{enemy.name} rolls a {enemy_roll}\n')
            time.sleep(1)
            if player_roll > enemy_roll:
                enemy.hp -= self.attack
                print(f'{self.name} attacks and {self.weapon}.\n')
                time.sleep(1)
                print(f'{enemy.name} loses {self.attack} health with {enemy.hp} health remaining.')
            elif enemy_roll > player_roll:
                self.hp -= enemy.attack
                print(f'{enemy.name} attacks and {enemy.weapon}.\n')
                time.sleep(1)
                print(f'{self.name} loses {enemy.attack} health with {self.hp} health remaining.')
            else:
                print('It\'s a Draw, roll again!')
            time.sleep(1)
        if self.hp > 0:
            time.sleep(1)
            print(f'\nYou defeat {enemy.name}!!!\n')
            time.sleep(2)
     
    def puzzle(self):
        riddles =[
            'What has to be broken before you can use it?\n',
            'I\'m tall when young, yet short when I\'m old, What am I?\n',
            'I\'m full of holes but still hold water?\n',
            'What has lots of eyes, but can\'t see?\n',
            'I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?\n'
            ]
        clues = [
            'Who first, me or the Chicken!',
            'I show you the way in the dark!',
            'My best friend is Patrick!',
            'You can cut me into chips',
            'I keep you warm at night and cook your food'
        ]
        answers = ['Egg', 'Candle', 'Sponge', 'Potato', 'Fire']
        attempts = 0
        wins = 0
        i = randint(0, len(riddles) - 1)
        print('O\'kay Here we go...\n')
        while attempts < 5 and wins < 3:
            print(f'You be havin\' {5 - attempts} attempts left\n')
            time.sleep(1)
            player_answer = get_input(riddles[i])
            time.sleep(1)
            if attempts == 2:
                print(f'Ok I will give you a clue... \n{clues[i]}\n')
                time.sleep(1)
            if player_answer == answers[i]:
                print(f'You be clever cookie!\n')
                time.sleep(1)
                wins += 1
                attempts = 0
                riddles.pop(i)
                clues.pop(i)
                answers.pop(i)
                i = randint(0, len(riddles) - 1)
                print(f'You have {wins} riddles solved!')
            else:
                print(f'You\'ll have to be thinkin harder dan dat!')
                attempts += 1
        if wins == 3:
            self.master_of_riddles = True
            print('\nYou be wiser than I thought. Blessed be your travels!')
            time.sleep(2)
        else: 
            print(f'\nYou not so bright aren\'t ya, da answer is {answers[i]}')
            time.sleep(2)

class Monster:
    def __init__(self, name, base_hp, attack, weapon):
        self.name = name
        self.base_hp = base_hp
        self.attack = attack
        self.weapon = weapon
        self.hp = base_hp

class RockPaperScissors:
    def game(self, player):
        player_wins = 0
        comp_wins = 0
        time.sleep(1)
        while player_wins != 3 and comp_wins != 3:
            user_input = get_input('\nLets play.. Rock, Paper or Scissors?: ')
            while user_input not in ('Rock', 'Paper', 'Scissors'):
                print('\nPlease enter either Rock, Paper or Scissors')
                user_input = get_input('')
            random_int = randint(1,3)
            if random_int == 1:
                comp_choice = 'Rock'
            elif random_int == 2:
                comp_choice = 'Paper'
            else:
                comp_choice = 'Scissors'
            time.sleep(1)
            print(f'\nOgre chooses {comp_choice}')
            time.sleep(1)
            if user_input == comp_choice:
                print('\nIts a tie, Go again!')
                continue
            if user_input == 'Rock' and comp_choice == 'Paper':
                comp_wins += 1
                print('\nAHA I win this one!')
            if user_input == 'Rock' and comp_choice == 'Scissors':
                player_wins += 1
                print('\nYou are better than I thought!')
            if user_input == 'Scissors' and comp_choice == 'Paper':
                player_wins += 1
                print('\nI knew I should have gone ROCK!')
            if user_input == 'Scissors' and comp_choice == 'Rock':
                comp_wins += 1
                print('\nI am so smart.. S M R T...')
            if user_input == 'Paper' and comp_choice == 'Rock':
                player_wins += 1
                print('\nYou must be cheating!')
            if user_input == 'Paper' and comp_choice == 'Scissors':
                comp_wins += 1
                print('I\'m going Rock next time I promise')
            time.sleep(1)
            print(f'\nYour wins: {player_wins}\nOgre wins: {comp_wins}')
        if player_wins == 3:
            time.sleep(1)
            print(f'\nI don\'t know how but you beat me {player.name}!')
            player.has_gem = True
        else:
            print(f'\nCome back when you\'ve had some practice {player.name}, NO gem for you!')

        