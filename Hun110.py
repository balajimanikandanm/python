N1 = int(input())
S= list(input().split())
A1 = []
for i in S:
  if int(i)==78 or int(i)==1 or int(i)==4:
    A1.append('+')
  elif int(i[-2:])==35:
    A1.append('-')
  elif int(i[0])==9 and int(i[len(i)-1])==4:
    A1.append('*')
  elif int(i[:3])==190:
    A1.append('?')
  else:
    A.append('*')
for i in A1:
  print(i)
