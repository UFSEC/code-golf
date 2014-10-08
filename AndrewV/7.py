import sys as s
x=s.argv
k=''
a=k.join(sorted(x[1]))
b=k.join(sorted(x[2]))
if a==b:print True
else:print False