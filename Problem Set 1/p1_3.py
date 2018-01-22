# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
#
#
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc


s = 'azcbobobegghakl'

a = 'abcdefghijklmnopqrstuvwxyz'
r1 = len(s)
r2 = len(a)
count = 0
l = 0
l_temp = ''

f = 0
temp = ''

for i in range(len(s)):
    for j in range(len(a)):
        if a[j] == s[i]:
            break

    r2 = len(a) - j

    for k in range(r1):
        for p in range(r2):
            if s[i+k] == a[j+p]:
                count += 1
                f = 1
                temp += s[i+k]
                break

        if f == 0:
            break
        r2 -= p
        j += p
        f = 0

    if count > l:
        l = count
        l_temp = temp

    count = 0
    r1 -= 1
    temp = ''

print('Longest substring in alphabetical order is: ' + str(l_temp))