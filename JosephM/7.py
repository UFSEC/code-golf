a = raw_input()
b = raw_input()
F = True
for x in (0,len(a)-1):
	if(a[x] not in b):
		F = False
print F