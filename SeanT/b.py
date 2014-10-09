import sys
import collections
print collections.Counter(sys.argv[1:]).most_common(1)[0][0]