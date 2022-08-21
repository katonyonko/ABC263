import io
import sys

_INPUT = """\
6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  C=[list(map(int,input().split())) for _ in range(2**N)]
  ans=[C[i][0] for i in range(2**N)]
  tmp=[max(C[2*i][0],C[2*i+1][0]) for i in range(2**(N-1))]
  for i in range(N-1):
    tmp2=[0]*(2**N)
    for j in range(2**N):
      t=j>>(i+1)
      tt=t-1 if t%2==1 else t+1
      tmp2[j]=C[j][i+1]-C[j][i]+ans[j]+tmp[tt]
    ans=tmp2
    tmp=[max([ans[l] for l in range(k*2**(i+2),(k+1)*2**(i+2))]) for k in range(2**(N-i-2))]
  print(tmp[0])