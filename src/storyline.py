from random import randint

class StoryChoice:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.progress = ''

    def choice(self):
        print(f'{self.question}')
        answer = input()
        if answer == self.answer:
            print('You Win')
            self.progress = 'win'
        else:
            print("You Lose")

class Player:
    hero_list = ['Warrior', 'Hunter', 'Mage']

    def customize(self):
        self.name = input('What is your name?')
        self.hero = input('Which hero would you like to play as? Warrior, Hunter or Mage...')

        while self.hero not in self.hero_list:
                print('Please choose from the list')
                self.hero = input('Which hero would you like to play as? Warrior, Hunter or Mage...')

        if self.hero == 'Warrior':
            self.hp = 100
            self.attack = 10
            self.weapon = 'Axe'

        elif self.hero == 'Hunter':
            self.hp = 60
            self.attack = 20
            self.weapon = 'Bow'

        else:
            self.hp = 50
            self.attack = 40
            self.weapon = 'Frostbolt'

    def __repr__(self):
        return f'{self.name}, {self.hero}, {self.hp}, {self.attack}, {self.weapon}'

    def battle(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            player_roll = randint(1,11)
            print(f'{self.name} rolls a {player_roll}')
            enemy_roll = randint(1,11)
            print(f'{enemy.name} rolls a {enemy_roll}')
            if player_roll > enemy_roll:
                enemy.hp -= self.attack
                print(f'You win! enemy loses {self.attack}health.')
            elif enemy_roll > player_roll:
                self.hp -= enemy.attack
                print(f'{enemy.name} wins! you lose {enemy.attack}health.')
            else:
                print('It\'s a Draw')
        if self.hp > 0:
            print('You are the winner!')
        else:
            print('You are the Loser!')
        
    def puzzle(self):
        riddles = [
            'What has to be broken before you can use it?',
            'I\'m tall when young yet short when I\'m old, What am I?',
            'I\'m full of holes but still hold water?'
            ]
        clues = [
            'Who first, me or the Chicken!',
            'I show you the way in the dark!',
            'My best friend is Patrick!'
        ]
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
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

