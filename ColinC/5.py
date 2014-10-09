from sys import argv as a
from collections import Counter as C
print C(a[1:]).most_common(1)[0][0]