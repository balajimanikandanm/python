n1=input()
s1=""
for i in range(len(n1)-1):
  for j in range(i+1,len(n1)+1):
    r=n1[i:j+1]
    
    if len(r)>len(s1) and r==r[::-1]:
            s1=r
print(s1)
