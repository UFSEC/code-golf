import sys, collections as b
print b.Counter(sys.argv[1:]).most_common()[0][0]