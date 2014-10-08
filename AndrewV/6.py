import sys as s
x = s.argv
for i in range(0,len(min(x[1], x[2]))/2):
	if not (x[1][i]==x[2][len(x[2])-1-i]):
		print False
		break
print True