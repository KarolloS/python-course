# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
#
# Write a program that uses these bounds and bisection search  to find the smallest monthly payment to the cent
# such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is
# (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.


balance = 320000
annualInterestRate = 0.2

def rb(b, i, p):
    bt = b
    for k in range(12):
        ub = bt - p
        bt = ub + i/12.0*ub
    return bt

p = 0
b = balance
eps = 0.01
l =  balance/12.0
u = (balance*(1+annualInterestRate/12.0)**12)/12.0

while abs(b) > eps:
    p = (u + l) / 2
    b = rb(balance, annualInterestRate, p)
    if b > eps:
        l = p
    else:
        u = p

print('Lowest Payment: ' + str(round(p, 2)))