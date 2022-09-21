import storyline as s
from random import randint

welcome = s.StoryChoice('Welcome to the Game, would you like to play?', 'Yes')
play_again = s.StoryChoice('Would you like to play again?', 'Yes', 'Y')
level_one = s.StoryChoice("You see a Dragon ahead, Do you attack?", 'Yes')
level_two = s.StoryChoice("You see a mysterious figure ahead do you proceed?", 'Yes')
player = s.Player()
dragon = s.Monster('Dragon', 100, 10)
def death(input):
    print(f'{input}, You have died')

def main():
    
    welcome.choice()
    if welcome.progress:
        player.hero_pick()
        while play_again.progress:
            player.set()
            level_one.choice()
            if level_one.progress:
                player.battle(dragon)
                if player.hp > 0:
                    level_two.choice()
                    if level_two.progress:
                        player.puzzle()
                    else:
                        death('The Troll boils you in a pot!')
                else:
                    death('The Dragon has beaten you in battle')
            else:
                death('You try and run but the Dragon hunts you down')
            play_again.choice()
    print('Thank you for playing! GoodBye')


if __name__ == '__main__':
    main()
