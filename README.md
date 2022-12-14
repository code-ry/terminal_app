# T1A3 Terminal Assignment Ryan Bussey 13366

## Presentation

https://vimeo.com/manage/videos/753499423

## Repository

https://github.com/code-ry/terminal_app

## Code Styling

The Code styling conventions that this application will adhere to are the PEP 8 guidlines referenced below.

https://peps.python.org/pep-0008/

## Features

### RockPaperScissors

An event where the user will play the computer at a game of Rock, paper scissors.

- The user will be prompted to enter either 'Rock' or 'Paper' or 'Scissors' and the value assigned to a variable.
- If the incorrect value was entered the user will be prompted to try again.
- A value for the computers choice will be randomly generated using random module.
- These values will be compared, a winner deduced and a counter for how many losses/wins will be incremented accordingly.
- This will repeat until one side has one 3 times and the game will end.
- By winning this event the player will recieve a reward which will be needed to progress

### Battle

An event where the user will battle a monster with in a 'dice-roll' turn based style fashion. The player and computer will each be randomly generated a value for dice roll between 1 and 10. Values will then be compared and a winner deduced by the highest value.

- The losing side will decrease in Health by the amount of attack the opposing player has. The battle ends when on side goes below 0 health.
- By winning this event the player will recieve a reward which will be needed to progress

### Puzzle

Along the journey the User will come across a mysterious character. To get past this character the user must complete answer a series of riddles. The computer will have acces to 6 different riddles with associated clues and answers. The computer will randomly generate a riddle and the user has 5 attempts to answer correctly. After 3 attempts a clue will be given to the user. The user must answer 3 riddles correctly to win the game. By winning this event the player will recieve a reward which will be needed to progress

- The riddles, clues and answers will be stored in lists to be accessed by an index number
- To select a riddle the computer will randomly generate a value between 0 and the length of the list
- This value will be used as the index to access the associated value
- Once used the riddle,answer and clue will be popped from the list as to not repeat.
- The user input will be compared against the correct value for validity
- Invalid responses will result in an incorrect answer.

## Implementation Plan

https://trello.com/invite/b/MsbMDOnQ/525ad056e87b76e646bbd8678684e49c/terminal-game

## Testing

test_player_class.py tests the funtioniality of when the user chooses which hero to play as.
Is an important function as it affects multiple attributes of the player being health, and attack which will in turn affect the battle event. player names are also referenced throughout the game and so this function must work correctly.

The tests assure the user input corresponds to the correct hero that the choice is assigned to. Three diffrent values are tested to ensure correct behaviour.

### test_player_class results
============================= test session starts ==============================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /mnt/c/projects/assignments/term1/T1A3/src
collected 3 items

test_player_class.py ...                                                 [100%]

============================== 3 passed in 0.96s ===============================

test_story_choice.py tests the behaviour of a user input when used in the narrative line in the game. The user is promted to choose a path and the resulting choice will effect the result. This is a very important feature as it is the main way of tracking progression through the game, whether the user lives or dies.

The tests performed ensure when a user inputs a value it is assigned correctly to the given path and the resulting behavior is expected. The three tests assert that the input values are correctly assigned, and the returned value is expected.

### test_story_choice results
============================= test session starts ==============================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /mnt/c/projects/assignments/term1/T1A3/src
collected 3 items

test_story_choice.py ...                                                 [100%]

============================== 3 passed in 0.86s ===============================

## Help Documentation

### Installation

Download the files by cloning my repository using the command in terminal:
git clone https://github.com/code-ry/terminal_app

establish pwd to /src directory.
install Python
Run bash_script.sh by typing following command in terminal(This will set up a virtual environment and install any packages required for running app):
./bash_script.sh

ENJOY!

### Dependencies

Python3 installed with following packages:
art==5.7
attrs==22.1.0
iniconfig==1.1.1
numpy==1.23.3
packaging==21.3
pluggy==1.0.0
py==1.11.0
pyparsing==3.0.9
pytest==7.1.3
tomli==2.0.1

### System/Hardware requirements

Windows/Linux/Mac OS
30 MB Hard Drive space
8 MB RAM

### How to Use App

When prompted a question, type into the terminal the desired answer and press enter.
To exit program type 'Quit' at any time.
