def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    import string

    rest = ''

    for char in string.ascii_lowercase:    #iterates over the alphabet

        if char not in lettersGuessed:       # removes the letters in the string from the alphabet
            rest += char

    return rest                 # Returns the results


# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# z= getAvailableLetters(lettersGuessed)
# print z