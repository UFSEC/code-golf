import sys as s
x = s.argv
p = x[1]
l = len(p)
for i in range(0,l/2):
	if not (p[i]==p[l-1-i]):
		print False
		break
print True