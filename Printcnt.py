rb=input()
t=''
for i in range(0,len(rb)-1,2):
  if int(rb[i+1])%2==0:
    t+=rb[i]*int(rb[i+1])
  else:
    t+=rb[i]+rb[i+1]
print(t)
