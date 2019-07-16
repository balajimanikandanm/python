lo,ve=input().split()
lo=str(lo)  
ve=int(ve)
L=[] 
for i in range(len(lo)-ve+1):
	L.append(lo[i:i+ve])  
print(*L)
