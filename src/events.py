import time
from random import randint
import storyline as s

class Event:
    def __init__(self, reward):
        self.reward = reward

class Puzzle(Event):

    def riddler(self, player):

        # Riddles, clues and answers stored in corresponding lists

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

        # Game-Logic: Using a randomly generated integer program can access matching from lists
        # Asks for user input, if matches correct answer wins is incremented until 3 and game ends
        # attempts reset upon successful answer
        # if Incorrect answer, attempts is decreased until 0 and game ends

        attempts = 0
        wins = 0
        i = randint(0, len(riddles) - 1)
        print('O\'kay Here we go...\n')
        while attempts < 5 and wins < 3:
            if attempts == 3:
                print(f'Ok I will give you a clue... {clues[i]}\n')
                time.sleep(1)
            print(f'You be havin\' {5 - attempts} attempts left\n')
            time.sleep(1)
            player_answer = s.get_input(riddles[i])
            time.sleep(1)

            if answers[i].lower() in player_answer.lower():
                print('You be a clever cookie!\n')
                time.sleep(1)
                wins += 1
                attempts = 0
                riddles.pop(i)
                clues.pop(i)
                answers.pop(i)
                i = randint(0, len(riddles) - 1)
                print(f'You have {wins} riddles solved!\n')
            else:
                print(f'You\'ll have to be thinkin harder dan dat {player.name}!\n')
                attempts += 1

        if wins == 3:
            player.badges.append(self.reward)
            time.sleep(1)
            print(f'{player.name} gains the badge [{self.reward}]\n')
            time.sleep(1)
            print(f'You be wiser than I thought {player.name}. Blessed be your travels!\n')
            time.sleep(2)
        else:
            print(f'You not so bright aren\'t ya, da answer is {answers[i]}\n')
            time.sleep(2)

class Battle(Event):

    # Battles 2 characters against each other in randomly generated dice roll format
    # Randomly generated numbers are stored in variables and then compared.
    # Whichever is higher wins and health is deducted according to winners attack.
    # Game ends when one character reaches 0 health

    def battle(self, player, enemy):
        s.get_input(f'{player.name} faces off with {enemy.name}.\n\nWhoever rolls a higher number, gets to attack.\n\n Press Enter to roll!\n')
        counter = 0
        enemy.hp = enemy.base_hp
        while player.hp > 0 and enemy.hp > 0:
            if counter > 0:
                s.get_input('\nPress Enter to Roll again!\n')
            counter += 1
            time.sleep(1)
            player_roll = randint(1,10)
            print(f'{player.name} rolls a {player_roll}\n')
            time.sleep(1)
            enemy_roll = randint(1,10)
            print(f'{enemy.name} rolls a {enemy_roll}\n')
            time.sleep(1)

            if player_roll > enemy_roll:
                enemy.hp -= player.attack
                print(f'{player.name} attacks and {player.weapon}.\n')
                time.sleep(1)
                print(f'{enemy.name} loses {player.attack} health with {enemy.hp} health remaining.')
            
            elif enemy_roll > player_roll:
                player.hp -= enemy.attack
                print(f'{enemy.name} attacks and {enemy.weapon}.\n')
                time.sleep(1)
                print(f'{player.name} loses {enemy.attack} health with {player.hp} health remaining.\n')
            
            else:
                print('It\'s a Draw, roll again!\n')
            time.sleep(1)

        # Assigns reward to player if successful

        if player.hp > 0:
            time.sleep(1)
            print(f'\n{player.name} defeats {enemy.name}!!!\n')
            player.badges.append(self.reward)
            time.sleep(1)
            print(f'{player.name} gains the badge [{self.reward}]\n')
            player.hp = player.base_hp
            time.sleep(2)
        else:
            print(f'{enemy.name} has defeated you in battle, {player.name} limps away in sorrow..\n')

class RockPaperScissors(Event):

    def game(self, player):
        player_wins = 0
        comp_wins = 0
        time.sleep(1)

        # Checks user_input and outputs error message if invalid input is detected

        while player_wins != 3 and comp_wins != 3:
            user_input = s.get_input('Lets play.. Rock, Paper or Scissors?: \n')
            try: 
                s.raise_exception(user_input, 'Rock', 'Paper','Scissors')
            except s.IncorrectValue:
                print('Please enter a valid value\n')

            while user_input not in ('Rock', 'Paper', 'Scissors'):
                print('Please enter either Rock, Paper or Scissors')
                user_input = s.get_input('')

            # Generates a value for the computer choice

            random_int = randint(1,3)
            if random_int == 1:
                comp_choice = 'Rock'
            elif random_int == 2:
                comp_choice = 'Paper'
            else:
                comp_choice = 'Scissors'

            time.sleep(1)
            print('\nRock...\n')
            time.sleep(1)
            print('Paper...\n')
            time.sleep(1)
            print('Scissors!\n')
            time.sleep(1)
            print(f'{player.name} chooses {user_input}\n')
            print(f'Ogre chooses {comp_choice}\n')
            time.sleep(1)
            
            # Compares user_input and comp_imput to formulate a winner in all scenarios

            if user_input == comp_choice:
                print('Its a tie, Go again!\n')
                continue
            if user_input == 'Rock' and comp_choice == 'Paper':
                comp_wins += 1
                print('AHA I win this one!\n')
            if user_input == 'Rock' and comp_choice == 'Scissors':
                player_wins += 1
                print('You are better than I thought!\n')
            if user_input == 'Scissors' and comp_choice == 'Paper':
                player_wins += 1
                print('I knew I should have gone ROCK!\n')
            if user_input == 'Scissors' and comp_choice == 'Rock':
                comp_wins += 1
                print('I am so smart.. S M R T...\n')
            if user_input == 'Paper' and comp_choice == 'Rock':
                player_wins += 1
                print('You must be cheating!\n')
            if user_input == 'Paper' and comp_choice == 'Scissors':
                comp_wins += 1
                print('I\'m going Rock next time I promise\n')
            time.sleep(1)
            print(f'Your wins: {player_wins}\nOgre wins: {comp_wins}\n')

        # Checks if player wins are sufficient and reward is assigned to player

        if player_wins == 3:
            time.sleep(1)
            print(f'I don\'t know how but you beat me {player.name} but you truely are more deserving of this {self.reward}!\n')
            player.badges.append(self.reward)
            time.sleep(1)
            print(f'{player.name} gains the item [{self.reward}]')

        else:
            print(f'Come back when you\'ve had some practice {player.name}, NO gem for you!\n')
        