import sys
a = sys.argv[1]
b = sys.argv[2]
c = 'True'
for x in range(0, len(b)):
    if a[x] != b[(len(b) - x - 1)]:
        c = 'False'
print c
