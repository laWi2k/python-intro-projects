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
isRunning = True


while tries > 0:
    if isRunning == False:
        break
    print(*wordInProgress)
    letter = input('Enter your guess: ')
    if len(letter) > 1:
        print('Write just one letter please')
    else:
        if word.find(letter) == -1:
            tries -= 1
            incorrectLetters.append(letter)
            hangman = hangmanConfig.guys[6 - tries]
            print(hangman)
        else:
            for i in range(0, len(word)):
                if letter == word[i]:
                    wordInProgress[i] = letter
                if str(wordInProgress).find('_') == -1:
                    print('You won!!!')
                    isRunning = False
                    break

    # clear_terminal()
if tries == 0:
    print('You lost!!!')