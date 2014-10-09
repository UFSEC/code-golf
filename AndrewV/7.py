import sys
x=sys.argv
k=''
s=sorted
j=k.join
c=False
if j(s(x[1]))==j(s(x[2])):c=True
print c