S,B=input().split()
temp=""
def string(n1):
   x=""
   for i in range(1,n1+1):
      x+=str(i)
   return x
if len(B)>len(S):
   S+=string(len(B)-len(S))
elif len(S)>len(B):
   B+=string(len(S)-len(B))
for i in range(len(S)):
   temp+=(S[i]+B[i])
print(temp)
