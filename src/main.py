import storyline as s
from random import randint
level_one = s.StoryChoice("Want to go Left or Right", 'left')
level_two = s.StoryChoice("Second choice Want to go Left or Right", 'right')
player = s.Player()
dragon = s.Monster('Dragon', 100, 10)
# play_again = level_one.choice()

def main():
    # player.customize()
    # player.battle(dragon)
    # level_one.choice()
    # if level_one.progress == 'win':
    #     level_two.choice()
    # player.puzzle()


if __name__ == '__main__':
    main()
