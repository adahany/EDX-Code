from ps3_hangman import chooseWord, wordlist
from Hangman_Part1 import isWordGuessed
from Hangman_Part2 import getGuessedWord
from Hangman_Part3 import getAvailableLetters


def hangman(secretWord):

    lettersGuessed = []
    pr = 0
    guesses = 8

    print'Welcome to the game, Hangman!'
    print'I am thinking of a word that is %i letters long.' % len(secretWord)
    print '-----------'

    while abs(guesses) > 0:

        print 'You have %i guesses left' %guesses

###################################################### show the user the available letters they can choose from

        avail = getAvailableLetters(lettersGuessed)
        print 'Available letters: %s' % avail

###################################################### Allows the user to enter a letter

        lett = raw_input('Please guess a letter: ')
        lett = lett.lower()

###################################################### Checks if the letter has been entered before in the list


        if any(lett in s for s in lettersGuessed):
            print"Oops! You've already guessed that letter: %s " %pr
            print '-----------'

####################################################### adds the letter to the list and checks if it is in the secret word or not

        else:

            lettersGuessed.append(lett)        # adds the letter entered in the list
            pr = getGuessedWord(secretWord,lettersGuessed)         #function is called compared if you made the right guess or not

            if lett in secretWord:               # This test for if whatever entered is a letter then calls a function getGuessedWod
                print 'Good guess: %s ' % pr
                print '-----------'
            elif lett not in secretWord:
                guesses -= 1
                print 'Oops! That letter is not in my word: %s ' % pr
                print '-----------'

############################################################ test if you have guessed the word correctly

        test = isWordGuessed(secretWord,lettersGuessed)
        if test == True:
            print 'Congratulations, you won!'
            return None

    print ' Sorry, you ran out of guesses. The word was %s.' %secretWord




# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# z= getAvailableLetters(lettersGuessed)
# print z

secretWord = chooseWord(wordlist).lower()
z = hangman(secretWord)

