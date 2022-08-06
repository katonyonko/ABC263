import io
import sys

_INPUT = """\
6
5 4 3
5 5 0 6 3
4 10 10
1 2 3 4
10 -5 -3
9 -6 10 -1 2 10 -1 7 -15 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,L,R=map(int,input().split())
  A=list(map(int,input().split()))
  B=[0]+[L-A[i] for i in range(N)]
  C=[R-A[i] for i in range(N)]
  r=[0]
  c=0
  for i in reversed(range(N)):
    c+=C[i]
    r.append(min(r[-1],c))
  r=r[::-1]
  s=sum(A)
  ans=s
  for i in range(N+1):
    s+=B[i]
    ans=min(ans,s+r[i])
  print(ans)