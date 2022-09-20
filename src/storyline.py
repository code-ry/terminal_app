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
class Character:
    # def __init__(self):
    #     self.name = ''
    hero_list = ['Warrior', 'Hunter', 'Mage']
    #     self.hero = ''
    #     self.hp = 0
    #     self.attack = 10
    #     self.weapon = ''
    
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