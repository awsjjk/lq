import math

n,m=map(int,input().split())
Ls = [int(x) for x in input().split()]

for i in range(m):
    index=Ls.index(max(Ls))
    half=math.ceil(Ls[index]/2)
    Ls.append(Ls[index]-half)
    Ls[index] = half

print(max(Ls))