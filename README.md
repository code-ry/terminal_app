# T1A3 Terminal Assignment Ryan Bussey 13366

## References

## Repository

https://github.com/code-ry/terminal_app

## Code Styling

The Code styling conventions that this application will adhere to are the PEP 8 guidlines referenced below.

https://peps.python.org/pep-0008/

## Features

### Items and Attributes

At the start of the game, the user can choose from a range of characters to customize their play style. Each character will have different strengths and weakness represented by attridutes which will effect game-play. The user will be able to choose a limited amount of items to carry which will also adjust their characters attributes. Throughout the game a user will come across different items with which they can swap out with current ones in their inventory.

### Battle

Throughout the game the user will encounter enemies that they must overcome to progress. To overcome the enemy the user will battle the computer in a turn based random 'dice-roll' style. Whoever rolls the highest number wins that attack and damage is dealt to the opposing side. The battle ends when one side is reduced to 0 health after an attack is made.

### Puzzle

Along the journey the User will come across a mysterious character. To get past this character the user must complete a puzzle. The mysterious character will choose a random 5 letter word from a selected list, then give the user a clue to what the word is. The user will have to guess the word in 5 tries or fail the test and suffer the consequences.

## Implementation Plan

https://trello.com/invite/b/MsbMDOnQ/525ad056e87b76e646bbd8678684e49c/terminal-game

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
When asked yes or no type 'yes' or simply type 'y' then enter.
To exit program type CTRL+C or when asked to play again type 'No'.