sa=input()
chee=True
if '@' not in sa:
	chee=False
if sa.count('@')>1 or sa.count('.')>1 and chee==True:
	chee=False
if len(sa[sa.index('@')+1:sa.index('.')])<4 or sa[sa.index('@')+1:sa.index('.')]!="gmail" and chee==True:
	chee=False
if len(sa[:sa.index('@')])<3 and chee==True:
	chee=False
if sa.endswith('.com')==False and chee==True:
	chee=False
if chee:
	print("YES")
else:
	print("NO")
