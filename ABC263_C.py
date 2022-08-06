import io
import sys

_INPUT = """\
6
2 3
3 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  res=[0]
  def sol(N,M):
    if N>0:
      for i in range(res[-1]+1,M+1):
        res.append(i)
        sol(N-1,M)
        res.pop()
    else:
      print(*res[1:])
  N,M=map(int,input().split())
  sol(N,M)