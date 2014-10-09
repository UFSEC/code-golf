import sys
import collections as c
print c.Counter(sys.argv[1:]).most_common()[0][0]