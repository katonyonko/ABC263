import io
import sys

_INPUT = """\
6
1 2 1 2 1
12 12 11 1 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X=list(map(int,input().split()))
  ans='Yes'
  for i in range(5):
    if X.count(X[i]) not in {2,3}: ans='No'
  print(ans)