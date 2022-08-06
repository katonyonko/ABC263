import io
import sys

_INPUT = """\
6
3
1 2
10
1 2 3 4 5 6 7 8 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  P=list(map(lambda x:int(x)-1,input().split()))
  ans=1
  now=N-2
  while P[now]!=0:
    now=P[now]-1
    ans+=1
  print(ans)