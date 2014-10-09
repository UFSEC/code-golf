import sys
a=sys.argv[1:]
print max(a,key=a.count)