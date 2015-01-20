__author__ = 'thebackd00r'


# def isVowel(s):
#
#     s = s.lower()
#     list1 = ['b', 'o']
#     count = 0
#     count1 =0
#     bob = ''
#     for letter in s:
#         if letter in list1:
#             bob += letter
#             count += 1
#             print count
#             print bob
#             if bob == 'bb':
#                 bob = letter
#                 count = 1
#             if count == 3:
#                 if bob == 'bob':
#                     count1 += 1
#                     bob = letter
#                     count = 1
#                 elif letter == 'b':
#                     bob = letter
#                     count = 1
#                 else:
#                     bob = ''
#                     count = 0
#     print 'Number of times bob occurs is: '+str(count1)
#     return count1
#
#
#
# z=isVowel('azcbobobegbobl')



s='bobobbobhgpboobobooxboobobobobbobobtjoboooboobzbob'
s = s.lower()
list1 = ['b', 'o']
count = 0
count1 = 0
bob = ''
for letter in s:
    if letter in list1:
        bob = bob+letter
        count += 1
        if letter =='o' and bob!='bo':
            bob = ''
            count = 0
        if bob == 'bb':
            bob = letter
            count = 1
        elif count == 3:
            if bob == 'bob':
                count1 += 1
                bob = letter
                count = 1
            elif letter == 'b':
                bob = letter
                count = 1
            else:
                bob = ''
                count = 0
    else :
        bob = ''
        count = 0
print 'Number of times bob occurs is: '+str(count1)