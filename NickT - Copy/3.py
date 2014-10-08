def f(a): return 0 if a == 0 else 1 if a == 1 else f(a-1)+f(a-2)
for x in range(12): print  f(x+1),