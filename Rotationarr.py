rb,sb=map(int,input().split())
l=[str(x) for x in input().split()]
b=l[sb:]+l[:sb]
print(' '.join(b))
