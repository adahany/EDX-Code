__author__ = 'thebackd00r'


balance = 999999  #how much you borrow from bank
annualInterestRate = 0.18    #how much interest in a year
remain = float(balance)
epsilon = 0.01
montlyinterest = (annualInterestRate/12.0)
lowerbound = balance / 12.0
upperbound = (balance * (1 + montlyinterest)**12)/12.0
minimum = (upperbound+lowerbound)/2

while abs(remain) >= epsilon:

    month = 0
    remain = float(balance)
    while month < 12:
        month += 1
        remain -= minimum
        interest = (annualInterestRate/12.0)*remain
        remain += interest

    if remain > epsilon :                 #paying less need to pay more
        lowerbound = minimum
        minimum = (upperbound+lowerbound)/2
    else:
        upperbound = minimum
        minimum = (upperbound+lowerbound)/2

print 'Lowest Payment: %.2f ' %round(minimum,2)