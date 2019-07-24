import sys,string
def dgtSum(nb) :
    sum1 = 0
    while nb :
        sum1 += nb%10
        nb //= 10
    return sum1

nb = int(input())
if nb <= 9:
    print(nb)
    sys.exit()
a = nb // 9
b = nb % 9
if b :
    s = str(b) + str('9') * a
else :
    s = str('9') * a
print(s)
