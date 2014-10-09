import sys
x=sys.argv
k=''
s=sorted
j=k.join
a=j(s(x[1]))
b=j(s(x[2]))
c=False
if a==b:c=True
print c