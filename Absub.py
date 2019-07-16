import sys,string, itertools

sb = input()
n = len(sb)
rb = n//2
for j in range(n-1,-1,-1) :
    #print('arr len = ', j+1)
    for i in range(0,n-j) :
        li, ri = i,j+i
        s1 = sb[li:ri+1]
        #print(li, ri, s1)
        for j in range(rb,0,-1) :
            s21 = 'ab'*j
            s22 = s21 + 'a'
            if s22 in sb :
                print(len(s22))
                sys.exit()
            elif s21 in sb :
                print(len(s21))
                sys.exit()
print(0)
