def f(a): return a if a <= 1 else f(a-1)+f(a-2)
for x in range(12): print  f(x+1),