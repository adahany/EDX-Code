def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    result = ''
    spac = '  _  '

    for char in secretWord.lower():

        if char in lettersGuessed:
            result += char
        else:
            result += spac

    return result

# secretWord= 'appre'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#lettersGuessed =[]
#z= getGuessedWord(secretWord,lettersGuessed)
#print z