import sys
a = sys.argv[1]
b = sys.argv[2]
F = True
for x in (0,len(a)-1):
	if(a[x] not in b):
		F = False
print F