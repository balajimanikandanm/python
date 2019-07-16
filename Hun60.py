t=int(input())
sb=[int(i) for i in input().split()]
rb=[int(i) for i in input().split()]
i=sb.index(sb[t-2])
j=rb.index(sb[i])
print(i-j)
