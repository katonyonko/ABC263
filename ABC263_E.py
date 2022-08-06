import io
import sys

_INPUT = """\
6
3
1 1
5
3 1 2 1
3
2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N=int(input())
  A=list(map(int,input().split()))
  dp=[0]*N
  adp=[0]*(N+1)
  deno=1
  for i in range(N-1):
    deno=(deno*A[i])%mod
  for i in reversed(range(N-1)):
    dp[i]=((adp[i+1]-adp[i+A[i]+1])*pow(A[i],mod-2,mod)+deno+deno*pow(A[i],mod-2,mod))%mod
    adp[i]=(adp[i+1]+dp[i])%mod
  print(dp[0]*pow(deno,mod-2,mod)%mod)