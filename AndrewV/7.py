import sys as s
x = s.argv
a = ''.join(sorted(x[1]))
b = ''.join(sorted(x[2]))
if a == b:print True
else:print False