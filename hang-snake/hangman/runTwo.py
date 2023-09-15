from common.util import clear_terminal
from random import randint
import dict
import hangmanConfig

word = dict.words[randint(0,len(dict.words)-1)]
tries = 6
incorrectLetters = []
correctLetters = []
wordInProgress = ['_']*len(word)
hangman = hangmanConfig.guys[6-tries]


while tries > 0:
    print(word)
    print(*wordInProgress)
    letter = input('Enter your guess: ')
    if len(letter) > 1 or type(letter) != 'str':
        print('Write just one letter please')
    else:
        if word.find(letter) == -1:
            tries -= 1
            incorrectLetters.append(letter)
            hangman = hangmanConfig.guys[6 - tries]
            print(hangman)
        else:
            tries = tries
            for i in len(word):
                if letter == word[i]:
                    wordInProgress[i] = letter

    # clear_terminal()
