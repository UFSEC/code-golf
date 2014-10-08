import sys
s=sys.argv
a=s[1]
b=s[2]
F=True
for x in (0,len(a)-1):
	if(a[x] not in b):F=False
print F