import math
def isprime(ss):
    if(ss ==2):
        return True
    elif(ss%2 == 0):
        return False
    else:
        for j in range(2,int(math.sqrt(ss)+1)):
            if(ss%j == 0):
                return False
        return True
b = int(input(""))
prime = []
for i in range(2,b):
    if(isprime(i)):
        prime.append(i)
if(len(prime)>0):
    if(prime[-1] == 97):
        print(" ".join(map(str,prime)),"")
    else:
        print(" ".join(map(str,prime)))
else:
    print(0)
