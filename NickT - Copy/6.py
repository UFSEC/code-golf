import sys
a=sys.argv[1]
b='True'
for c in range(len(a)):
	if a[c]!=a[len(a)-c-1]:b='False'
print b