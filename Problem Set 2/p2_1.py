# Write a program to calculate the credit card balance after one year if a person only pays
# the minimum monthly payment required by the credit card company each month.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
#
# For each month, calculate statements on the monthly payment and remaining balance.
# At the end of 12 months, print out the remaining balance.


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def rb(m, i, p):
    if m == 0:
        b = balance
        # print('month: ' + str(m) + ' balance: ' + str(b))
        return b
    else:
        ub = rb(m - 1, i, p) * (1 - p)
        b = round(ub + i / 12.0 * ub, 2)
        # print('month: ' + str(m) + ' balance: ' + str(b))
        return b


print('Remaining balance:', rb(12, annualInterestRate, monthlyPaymentRate))