def f(a):return a if a<2 else f(a-1)+f(a-2)
for a in range(12):print f(1+a),