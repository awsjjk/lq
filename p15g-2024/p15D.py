import math

n,m=map(int,input().split())
Ls = [int(x) for x in input().split()]

def check(x) :
    if x==0:return False
    cuts=0
    for length in Ls:
        cuts+=math.ceil(length/x)-1
    return cuts<=m

#solve:
left=1
right=max(Ls)
ans=right
while left<=right:
    mid=(left+right)//2
    if check(mid):
        ans=right
        right=mid-1
    else:
        left=mid+1

print(ans)

