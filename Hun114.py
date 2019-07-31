def PSUM(nu) :
    sum = 0
    while nu :
        sum += nu%10
        nu //= 10
    return sum

def isPrime(nu) :
    if nu==1 : return False
    if nu==2 or nu==3 : return True
    for i in range(2,nu) :
        if nu%i == 0 :
            return False
    return True

a,b = input().split()
a,b = int(a),int(b)
out = 0
for i in range(a,b+1) :
    sum = PSUM(i)
    if isPrime(sum) :
        out += 1
        
print(out)
