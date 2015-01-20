__author__ = 'thebackd00r'

s = 'xehzoysiscevmlstx'
s.lower()
conc = ''       #where the word is concatinated
word = ''      #variable where the exact word is stored
test = ''      #variable to test if in alphabetical order
for char in s:
    conc += char
    test = ''.join(sorted(conc))
    if test == conc and len(test) > len(word):
        word = test
    else:
        conc = conc[1:]         #remove first letter and keep the rest
print 'Longest substring in alphabetical order is: ' +str(word)
