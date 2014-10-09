import sys
from collections import Counter as C
print C(sys.argv[1:]).most_common(1)[0][0]