import art
import storyline as s
from random import randint
import time
import numpy as np

welcome = s.StoryChoice('''Welcome to GemQuest, make your way through the unknown lands to find the treasure!\n
                           To quit at any time type 'quit'\n Press Enter to begin...''', '', '')
play_again = s.PlayAgain('Would you like to play again?', 'Yes', 'Y')
level_one = s.StoryChoice("You see a Dragon ahead, Do you attack?", 'Yes','You try and run but the Dragon hunts you down')
level_two = s.StoryChoice("You see a mysterious figure ahead do you proceed?", 'Yes', 'The Troll boils you in a pot!')
player = s.Player()
dragon = s.Monster('Dragon', 100, 10, 'breathes a gigantic Fireball')
first_story = s.StoryLine('You begin your quest by heading out of town into the forest.')
first_story.add_line('Then you come across a cave with a dragon.')

def main():
    try:
        while True:
            art.tprint("GemQuest")
            welcome.choice()
            time.sleep(1)
            if welcome.progress:
                player.hero_pick()
                player.set()
                first_story.concat_lines()
                level_one.choice()
                time.sleep(1)
                if level_one.progress:
                    player.battle(dragon)
                    time.sleep(1)
                    if player.hp > 0:
                        level_two.choice()
                        time.sleep(1)
                        if level_two.progress:
                            player.puzzle()
                        else:
                            print(level_two.fail)
                    else:
                        print(level_one.fail)
                else:
                    print(level_one.fail)
            play_again.choice()
    except KeyboardInterrupt:
        print("Thanks for playing! GoodBye") 

if __name__ == '__main__':
    main()
