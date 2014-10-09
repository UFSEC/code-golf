import sys
x = sys.argv
p = x[1]
l = len(p)
for i in range(0,l/2):
	if p[i]!=p[l-1-i]:
		print False	
		break
print True