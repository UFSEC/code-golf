import sys
a=sys.argv[1:]
print max(set(a),key=a.count)