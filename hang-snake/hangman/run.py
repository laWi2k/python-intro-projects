from common.util import clear_terminal
from random import randint
import dict
import hangmanConfig


def createSecret():
    return str(dict.words[randint(0,len(dict.words)-1)])

secretWord = createSecret()
tries = 6
incorrectLetters = []
correctLetters = []
wordInProgress = ['_']*len(secretWord)
hangman = hangmanConfig.guys[6-tries]

def play():
    print(secretWord)
    print(*wordInProgress)
    global tries
    global hangman
    letter = input('Enter your guess: ')
    if len(letter)>1 or type(letter) != 'str':
        return 'Write just one letter please'
    else:
        if secretWord.find(letter) == -1:
            tries -= 1
            incorrectLetters.append(letter)
            hangman = hangmanConfig.guys[6 - tries]
            print(hangman)
        else:
            for i in len(secretWord):
                if letter == secretWord[i]:
                    wordInProgress[i] = letter
        return

while tries > 0:
    play()

    # clear_terminal()
    # print(FIELD)
