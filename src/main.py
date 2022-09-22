import art
import time
import storyline as s
import numpy as np
from random import randint



welcome = s.StoryChoice('''Welcome to GemQuest, make your way through the unknown lands to find the treasure!\n
                           To quit at any time type 'Quit'\n Type 'Start' to begin... \n''', 'Start', 'Quit', '')
first_story = s.StoryLine('\nYou begin your quest by heading out of town into the forest.')
first_story.add_line('Then you come across a cave with a Dragon.\n')
level_one = s.StoryChoice("Do you attack the Dragon? Y or N: ", 'Y','N', 'The Dragon melts you with his firey breath! \n You die a toasty death!\n')
second_story = s.StoryLine('You are pleased with yourself that you overcome the Dragon and continue along your path.')
second_story.add_line('\nBefore long you come across a bridge and begin to cross...')
second_story.add_line("\nA Troll jumps out! 'Who dare be crossin' my bridge? Answer 3 O' me riddles correctly and I shall let you past.'")
level_two = s.StoryChoice('\nDo you want to answer me riddles? Y or N: \n', 'Y', 'N', 'The Troll picks you up and boils you in his pot for dinner!')
third_story = s.StoryLine("\nYou adopt the nickname of 'Master of Riddles' and continue on your merry way")
third_story.add_line('\nOn the horizon is a glimmering stone atop a mountain, This must be the Gem you are looking for!')
third_story.add_line('\nYou almost reach the top before you are stopped by an Ogre...')
third_story.add_line("\n'You won\'t be getting your little hands on me gem little one!'")
third_story.add_line('\nBut I a friendly Ogre so I give you a chance... Lets play a game')
third_story.add_line('\nMy favourite game, first one to 3 gets the shiney Gem!')
ending = s.StoryLine('\nYou gleefully skip off with your treasure and return to the Village to show your friends!')
ending.add_line('\nTHE END')

play_again = s.PlayAgain('Would you like to play again? Y or N: ', 'Y', 'N',)

player = s.Player()
dragon = s.Monster('The Dragon', 100, 10, 'breathes a gigantic Fireball')
final_boss = s.RockPaperScissors()

def main():
    try:
        while True:
            art.tprint("GemQuest")
            welcome.choice()
            time.sleep(1)
            if welcome.progress:
                player.hero_pick()
                player.set()
                time.sleep(1)
                first_story.concat_lines()
                level_one.choice()
                time.sleep(1)
                if level_one.progress:
                    player.battle(dragon)
                    if player.hp > 0:
                        second_story.concat_lines()
                        level_two.choice()
                        time.sleep(1)
                        if level_two.progress:
                            player.puzzle()
                            if player.master_of_riddles:
                                third_story.concat_lines()
                                final_boss.game(player)
                                if player.has_gem:
                                    ending.concat_lines()
                        else:
                            print(level_two.death_message)
                    else:
                        print(level_one.death_message)
                else:
                    print(level_one.death_message)
            play_again.choice()
    except KeyboardInterrupt:
        time.sleep(1)
        print("\nThanks for playing! Good Bye") 

if __name__ == '__main__':
    main()
