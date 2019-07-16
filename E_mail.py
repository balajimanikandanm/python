sa1=input()
chee=True
if '@' not in sa1:
	chee=False
if sa1.count('@')>1 or sa1.count('.')>1 and chee==True:
	chee=False
if len(sa1[sa1.index('@')+1:sa1.index('.')])<4 or sa1[sa1.index('@')+1:sa1.index('.')]!="gmail" and chee==True:
	chee=False
if len(sa1[:sa1.index('@')])<3 and chee==True:
	chee=False
if sa1.endswith('.com')==False and chee==True:
	chee=False
if chee:
	print("YES")
else:
	print("NO")
