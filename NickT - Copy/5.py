import sys 
a=str(sys.argv).split(", ")
b=0
c=""
d={}
for e in range(1,len(a)):
	f=a[e]
	if d.has_key(f):
		d[f]=d[f]+1
		if d[f]>b:
			d[f]
			c=f
	else:d[f]=0
print c