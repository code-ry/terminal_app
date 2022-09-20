import storyline as s

level_one = s.StoryChoice("Want to go Left or Right", 'left')
level_two = s.StoryChoice("Second choice Want to go Left or Right", 'right')
player = s.Character()
# play_again = level_one.choice()

def main():
    player.customize()
    print(player.__repr__)
    # level_one.choice()
    # if level_one.progress == 'win':
    #     level_two.choice()

if __name__ == '__main__':
    main()
