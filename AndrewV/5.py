import sys as s
x = str(s.argv).split("', '")
a = 0
b = ""
m = {}
for i in range(1,len(x)):
	c = x[i]
	if m.has_key(c):
		m[c] = m[c] + 1
		if m[c] > a: 
			m[c]
			b = c
	else: m[c] = 0
print b
