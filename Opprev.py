sr=input()
sr=sr.replace(".","")
lo=sr.split()
k=""
for i in range(1,len(lo)+1):
    if i%2!=0:
        k=k+lo[i-1][::-1]+" "
    else:
        k=k+lo[i-1]+" "
print(k.strip())        
#rev_at_odd
