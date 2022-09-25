import art
import time
import storyline as s
import events as e

# StoryLine content

welcome = s.StoryChoice('''Welcome to GemQuest, make your way through the unknown lands to find the treasure!\n
                           To quit at any time type 'Quit'\n Type 'Start' to begin... \n''', 'Start', 'Quit')
first_story = s.StoryLine('You begin your quest by heading out of town into the forest.\n')
first_story.add_line('The air is fresh and the birds are chirping, maybe you can find this Gem everyone is talking about. \n')
first_story.add_line('Before long you come across a cave, this could have the treasure you are looking for... \n')
level_one = s.StoryChoice("Do you dare enter the cave? Y or N: \n", 'Y','N')
battle_prelude = s.StoryLine('You dont get far into the cave before you realise it is home to a Dragon!\n')
battle_prelude.add_line('Its too late to run now, you must battle the dragon by rolling a 10-side dice.\n')
second_story = s.StoryLine('You are pleased with yourself that you overcome the Dragon and continue along your path.\n')
second_story.add_line('Before long you come across a bridge and begin to cross...\n')
second_story.add_line("A Troll jumps out! 'Who dare be crossin' my bridge? Answer 3 O' me riddles correctly and I shall let you past.'\n")
level_two = s.StoryChoice('Do you want to answer me riddles? Y or N: \n', 'Y', 'N')
third_story = s.StoryLine("You continue on your merry way across the bridge and into the hills\n")
third_story.add_line('On the horizon is a glimmering stone atop a mountain, This must be the Gem you are looking for!\n')
third_story.add_line('You almost reach the top before you are stopped by an Ogre...\n')
third_story.add_line("'You won\'t be getting your little hands on me gem little one!'\n")
third_story.add_line('But I a friendly Ogre so I give you a chance... Lets play a game\n')
third_story.add_line('My favourite game is Rock, Paper Scissors! first one to 3 gets the shiney Gem!\n')
happy_ending = s.StoryLine('\nYou gleefully skip off with your treasure and return to the Village to show your friends!\n')
happy_ending.add_line('\nTHE END\n')
sad_ending = s.StoryLine('\n You were out rocked, out papered and out scissored.\n')
sad_ending.add_line('You wander slowly back to town to practice against the other villagers. Hoping one day to return...\n')
sad_ending.add_line('\nTHE END... for now\n')
death_message = s.DeathMessage('\nYou decide to wander down the creek where you get swallowed by giant Toads..\n')
death_message.add_line('\nYou turn around and follow a trail into the woods, you get eaten by a Deer...\n')
death_message.add_line('\nYou head out into the clearing where an Eagle swoops down and carries you away. Forever...\n')
death_message.add_line('\nYou run away so quickly you trip and fall into a deep puddle and drown...\n')
death_message.add_line('\nYou find your way into an Gnomes garden and eat his poison berries, not good...\n')
death_message.add_line('\nYou decide to go for a swim in the nearby lake and get eaten by a Giant lake worm...\n')
play_again = s.PlayAgain('Would you like to play again? Y or N: \n', 'Y', 'N')

# Character and event instances
player = s.Player()
brimly = s.Character('Brimly the Fierce', 100, 30, 'Swings a crushing Axe')
mokimo = s.Character('Mokimo the Agile', 60, 40, 'Fires a mighty Long-Bow')
ailwyn = s.Character('Ailwyn the Powerful', 30, 50, 'Casts a barrage of Frostbolts')
dragon = s.Character('The Dragon', 100, 10, 'breathes a gigantic Fireball')
level_one_battle = e.Battle('Slayer of Dragon')
level_two_puzzle = e.Puzzle('Master of Riddles')
final_boss = e.RockPaperScissors('Gem')

def play_again_func():
    time.sleep(1)
    death_message.random_death()
    play_again.choice()

def main():
    # try statement to enable quit function when KeyboardInterrupt is called
    try:
        while True:
            art.tprint("Gem-Quest")
            welcome.choice()
            time.sleep(1)
            if welcome.progress is False:
                raise KeyboardInterrupt
            player.hero_pick(brimly, mokimo, ailwyn)
            player.set()
            time.sleep(1)
            first_story.concat_lines()
            level_one.choice()
            time.sleep(1)
            if level_one.progress is False:
                play_again_func()
                continue
            battle_prelude.concat_lines()
            level_one_battle.battle(player,dragon)
            if level_one_battle.reward not in player.badges:
                play_again_func()
                continue
            second_story.concat_lines()
            level_two.choice()
            time.sleep(1)
            if level_two.progress is False:
                play_again_func()
                continue
            level_two_puzzle.riddler(player)
            if level_two_puzzle.reward not in player.badges:
                play_again_func()
                continue
            third_story.concat_lines()
            final_boss.game(player)
            if final_boss.reward not in player.badges:
                play_again_func()
                continue
            time.sleep(1)
            happy_ending.concat_lines()
            play_again.choice()

    except KeyboardInterrupt:
        time.sleep(1)
        print("\nThanks for playing... Cheerio!\n")

if __name__ == '__main__':
    main()
