
import sys
n,m=sys.stdin.readline().strip().split()
li=list(map(int,sys.stdin.readline().strip().split()))
lights=list(set(li))
lights.sort()
length=len(lights)

#dp[i][0]已处理i个时，下一个点亮，dp[i][1]下一个不点亮

dp=[[0,0] for _ in range(len(lights))]

dp[0][0]=1
dp[0][1]=0

print(lights)

max_prev=0
for i in range(1,length):
    curr = lights[i]
    prev = lights[i-1]

    if curr-prev > 1:   #不相邻
        max_prev=max(dp[i-1][0],dp[i-1][1])
        dp[i][0]=max_prev+1
        dp[i][1]=max_prev
    else:   #相邻
        dp[i][0] = dp[i-1][1] +1
        dp[i][1] = max(dp[i-1][0],dp[i-1][1])

print(max(dp[-1][0],dp[-1][1]))
