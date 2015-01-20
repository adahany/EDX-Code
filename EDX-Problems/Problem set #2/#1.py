__author__ = 'thebackd00r'

balance = 4213  #how much you borrow from bank
annualInterestRate = 0.2    #how much interest in a year
monthlyPaymentRate = 0.04   #how much should be paid each mont minimum

month = 0    #number of months
remain = float(balance)
minimum = 0.0
paid = 0.0
while month < 12:

    month += 1

    minimum = remain * monthlyPaymentRate
    remain -= minimum
    interest = (annualInterestRate/12.0) * remain
    remain += interest
    paid += minimum
    print 'Month: %i ' %month
    print 'Minimum monthly payment: %.2f ' %round(minimum,2)
    print 'Remaining balance: %.2f ' %round(remain,2)


print 'Total paid: %.2f ' %round(paid,2)
print 'Remaining balance: %.2f ' %round(remain,2)

