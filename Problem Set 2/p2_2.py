# Now write a program that calculates the minimum fixed monthly payment needed in order
# pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does
# not change each month, but instead is a constant amount that will be paid each month.
#
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal


balance = 3329
annualInterestRate = 0.2

def rb(b, i, p):
    bt = b
    for k in range(12):
        ub = bt - p
        bt = ub + i/12.0*ub
    return bt

p = 0
b = balance
while b > 0:
    p += 10
    b = rb(balance, annualInterestRate, p)

print('Lowest Payment: ' + str(p))